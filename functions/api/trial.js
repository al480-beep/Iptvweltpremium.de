// Cloudflare Pages Function: POST /api/trial – fully automatic free trial.
//
// 1. Creates a demo M3U line in the Trex activation panel (sub=99 uses one demo ticket),
//    with the panel note "Trial / iptvweltpremium.de / email | phone".
// 2. Emails the logins to the customer through Resend and a copy to kontakt@.
// 3. Schedules a reminder with the price list at Resend, sent REMINDER_HOURS before the trial ends.
//    An order from the same e-mail address cancels it (see order.js).
// If the panel refuses (for example no demo tickets left), the request is emailed to kontakt@
// so the logins can be sent by hand, and the customer still gets the success screen.
//
// Environment variables (Cloudflare Pages → Settings → Variables and Secrets):
//   TREX_API_KEY    required – Developer API key from activationpanel.net → Profile / API
//   RESEND_API_KEY  required – API key from resend.com (domain iptvweltpremium.de verified there)
//   TREX_SERVER     optional – server URL given to customers (default http://line.trxdnscloud.ru)
//   TREX_TEMPLATE   optional – name of the panel template/bouquet to use (default "Germany")
//   TREX_PACK       optional – fixed package id (or "all"); skips the lookup by name
//   TREX_API_URL    optional – API endpoint (default https://activationpanel.net/api/api.php)
//   TRIAL_HOURS     optional – how long a demo line lasts (default 24)
//   REMINDER_HOURS  optional – hours before the end to send the reminder (default 12, 0 = no reminder)
//   TRIAL_TO        optional – internal copy (default kontakt@iptvweltpremium.de)
//   TRIAL_FROM      optional – sender (default "IPTV Welt Premium <kontakt@iptvweltpremium.de>")
//   TRIAL_IP_LIMIT  optional – max trials per IP address per hour, against bots (default 5)
// KV binding (optional, strongly recommended): TRIAL_KV – remembers each customer's latest trial so order mails can
// show it, a repeat trial replaces the old reminder, and the per-IP limit works. Customers may request several trials.
import { readContact, json, sendMail, cancelMail, mailFrom, mailTo, findTrial } from "./_shared.js";
import { trialCustomerMail, reminderMail, internalMail, berlinTime } from "./_emails.js";

const API_URLS = ["https://activationpanel.net/api/api.php", "https://activationpanel.ru/api/api.php"];
const DAY = 86400;
const HOUR = 3600 * 1000;

async function trex(env, params) {
  const urls = env.TREX_API_URL ? [env.TREX_API_URL] : API_URLS;
  let lastErr;
  for (const base of urls) {
    try {
      const qs = new URLSearchParams({ ...params, api_key: env.TREX_API_KEY });
      const r = await fetch(`${base}?${qs}`, { headers: { Accept: "application/json" } });
      const text = await r.text();
      const data = JSON.parse(text);
      return Array.isArray(data) ? data : [data];
    } catch (err) {
      lastErr = err; // host down or not JSON: try the next host
    }
  }
  throw lastErr || new Error("trex unreachable");
}

async function findPack(env) {
  if (env.TREX_PACK) return String(env.TREX_PACK);
  const wanted = String(env.TREX_TEMPLATE || "Germany").trim().toLowerCase();
  try {
    const list = await trex(env, { action: "bouquet" });
    const hit = list.find((b) => String(b.name || "").trim().toLowerCase() === wanted);
    if (hit?.id) return String(hit.id);
    console.warn(`trex: template "${wanted}" not found, using all bouquets`);
  } catch (err) {
    console.error("trex bouquet lookup failed", err);
  }
  return "all";
}

async function createDemo(env, c) {
  const pack = await findPack(env);
  const note = `Trial / iptvweltpremium.de / ${c.email} | ${c.dial}${c.phone}`.slice(0, 200);
  // The API documents "note"; "notes" is sent as well in case the panel reads that name.
  const [res] = await trex(env, { action: "new", type: "m3u", sub: "99", pack, note, notes: note });
  if (!res || String(res.status) !== "true" || !res.url) {
    throw new Error(`trex refused: ${res?.message || res?.messasge || JSON.stringify(res)}`);
  }
  // The panel returns the m3u link on its own domain (for this reseller it came back as "http://get.php?..."),
  // so customers get the fixed server instead.
  const params = new URL(res.url, "http://x").searchParams;
  const username = params.get("username") || "";
  const password = params.get("password") || "";
  const server = String(env.TREX_SERVER || "http://line.trxdnscloud.ru").replace(/\/+$/, "");
  const qs = new URLSearchParams({ username, password, type: "m3u_plus", output: "ts" });
  return { pack, note, userId: res.user_id || "", username, password, server, m3u: `${server}/get.php?${qs}` };
}

const summary = (c) => `Trial / iptvweltpremium.de / ${c.firstName} / ${c.email} / ${c.dial}${c.phone}`;

const contactRows = (c) => [
  ["Vorname", c.firstName],
  ["E-Mail", c.email],
  ["Telefon / WhatsApp", `${c.dial} ${c.phone} (${c.country})`],
  ["Notizen", c.notes || "–"],
];

export async function onRequestPost({ request, env }) {
  const { error, contact: c } = await readContact(request);
  if (error) return error;
  if (!env.TREX_API_KEY || !env.RESEND_API_KEY) return json({ error: "not_configured" }, 503);

  const to = mailTo(env);
  const from = mailFrom(env);
  const ip = request.headers.get("CF-Connecting-IP") || "";
  const keys = [`e:${c.email.toLowerCase()}`, `p:${c.dial}${c.phone}`];

  // Customers may request a trial as often as they like; only bots hammering from one IP are slowed down.
  const ipKey = ip && `ip:${ip}`;
  if (env.TRIAL_KV && ipKey) {
    const count = Number(await env.TRIAL_KV.get(ipKey)) || 0;
    if (count >= Number(env.TRIAL_IP_LIMIT || 5)) return json({ error: "rate_limited" }, 429);
    await env.TRIAL_KV.put(ipKey, String(count + 1), { expirationTtl: 3600 });
  }
  const previous = await findTrial(env, c.email, `${c.dial}${c.phone}`).catch(() => null);

  let line;
  try {
    line = await createDemo(env, c);
  } catch (err) {
    console.error(err);
    // Panel refused: hand the request to the team so nobody is lost.
    try {
      await sendMail(env, {
        from, to: [to], reply_to: c.email,
        subject: `MANUELL senden – ${summary(c)}`,
        html: internalMail(summary(c), [
          ["Status", "Automatischer Test fehlgeschlagen, bitte Zugangsdaten manuell senden"],
          ["Fehler", err.message],
          ...contactRows(c),
        ]),
      });
      return json({ ok: true, manual: true });
    } catch (mailErr) {
      console.error(mailErr);
      return json({ error: "send_failed" }, 502);
    }
  }

  const now = new Date();
  const expires = new Date(now.getTime() + Number(env.TRIAL_HOURS || 24) * HOUR);
  const internalRows = [
    ["Benutzername", line.username],
    ["Passwort", line.password],
    ["Server-URL", line.server],
    ["M3U", line.m3u],
    ["Läuft ab", berlinTime(expires)],
    ["Panel-ID", `${line.userId} · Paket ${line.pack}`],
    ["Panel-Notiz", line.note],
    ...contactRows(c),
  ];

  try {
    await sendMail(env, {
      from, to: [c.email], reply_to: to,
      subject: `🎉 ${c.firstName}, Ihr kostenloser Testzugang ist bereit – IPTV Welt Premium`,
      html: trialCustomerMail(c, line, expires),
    });
  } catch (err) {
    console.error(err);
    await sendMail(env, {
      from, to: [to], reply_to: c.email,
      subject: `E-Mail an Kunden FEHLGESCHLAGEN – ${summary(c)}`,
      html: internalMail(summary(c), [["Status", "Test erstellt, aber die E-Mail an den Kunden ging nicht raus. Bitte Zugangsdaten manuell senden."], ...internalRows]),
    }).catch(console.error);
    await remember(env, keys, c, line, now, expires, "");
    return json({ ok: true, manual: true });
  }

  // Reminder with the price list, sent by Resend shortly before the trial ends.
  let reminderId = "";
  const before = Number(env.REMINDER_HOURS ?? 12);
  if (before > 0) {
    const at = new Date(Math.max(expires.getTime() - before * HOUR, now.getTime() + HOUR));
    try {
      reminderId = await sendMail(env, {
        from, to: [c.email], reply_to: to,
        subject: `⏳ ${c.firstName}, Ihr Testzugang läuft bald ab – jetzt weiterschauen`,
        html: reminderMail(c.firstName, expires),
        scheduled_at: at.toISOString(),
      });
      internalRows.splice(5, 0, ["Erinnerung", berlinTime(at)]);
    } catch (err) {
      console.error("reminder not scheduled", err);
      internalRows.splice(5, 0, ["Erinnerung", `nicht geplant: ${err.message}`]);
    }
  }

  // A repeat trial gets one reminder only: drop the one planned for the earlier trial.
  if (previous?.reminderId && previous.reminderId !== reminderId) await cancelMail(env, previous.reminderId).catch(() => {});
  await remember(env, keys, c, line, now, expires, reminderId);
  await sendMail(env, {
    from, to: [to], reply_to: c.email,
    subject: summary(c),
    html: internalMail(summary(c), internalRows),
  }).catch(console.error);
  return json({ ok: true });
}

async function remember(env, keys, c, line, now, expires, reminderId) {
  if (!env.TRIAL_KV) return;
  const record = JSON.stringify({ created: now.toISOString(), expires: expires.toISOString(), username: line.username, firstName: c.firstName, reminderId });
  await Promise.all(keys.map((k) => env.TRIAL_KV.put(k, record, { expirationTtl: 90 * DAY })));
}
