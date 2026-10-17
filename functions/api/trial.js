// Cloudflare Pages Function: POST /api/trial – fully automatic free trial.
//
// 1. Creates a demo M3U line in the Trex activation panel (sub=99 uses one demo ticket).
// 2. Emails the logins to the customer through Resend and a copy to kontakt@.
// If the panel refuses (for example no demo tickets left), the request is emailed to kontakt@
// so the logins can be sent by hand, and the customer still gets the success screen.
//
// Environment variables (Cloudflare Pages → Settings → Variables and Secrets):
//   TREX_API_KEY    required – Developer API key from activationpanel.net → Profile / API
//   RESEND_API_KEY  required – API key from resend.com (domain iptvweltpremium.de verified there)
//   TREX_TEMPLATE   optional – name of the panel template/bouquet to use (default "Germany")
//   TREX_PACK       optional – fixed package id (or "all"); skips the lookup by name
//   TREX_API_URL    optional – API endpoint (default https://activationpanel.net/api/api.php)
//   TRIAL_TO        optional – internal copy (default kontakt@iptvweltpremium.de)
//   TRIAL_FROM      optional – sender (default "IPTV Welt Premium <kontakt@iptvweltpremium.de>")
// KV binding (optional, strongly recommended): TRIAL_KV – allows one trial per e-mail, phone and IP.
import { readContact, json, esc } from "./_shared.js";

const API_URLS = ["https://activationpanel.net/api/api.php", "https://activationpanel.ru/api/api.php"];
const DAY = 86400;

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
  const [res] = await trex(env, {
    action: "new",
    type: "m3u",
    sub: "99",
    pack,
    note: `Website-Test ${c.firstName} ${c.email} ${c.dial}${c.phone}`.slice(0, 200),
  });
  if (!res || String(res.status) !== "true" || !res.url) {
    throw new Error(`trex refused: ${res?.message || res?.messasge || JSON.stringify(res)}`);
  }
  const u = new URL(res.url);
  return {
    pack,
    userId: res.user_id || "",
    username: u.searchParams.get("username") || "",
    password: u.searchParams.get("password") || "",
    server: u.origin,
    m3u: res.url,
  };
}

async function sendMail(env, msg) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(msg),
  });
  if (!r.ok) throw new Error(`resend ${r.status}: ${await r.text()}`);
}

const customerHtml = (c, l) => `<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.6;color:#111">
<p>Hallo ${esc(c.firstName)},</p>
<p>vielen Dank für Ihr Interesse an IPTV Welt Premium! Ihr kostenloser Testzugang ist bereit:</p>
<table cellpadding="8" style="border-collapse:collapse;background:#f3f6fb;border-radius:8px">
<tr><td><b>Server-URL</b></td><td>${esc(l.server)}</td></tr>
<tr><td><b>Benutzername</b></td><td>${esc(l.username)}</td></tr>
<tr><td><b>Passwort</b></td><td>${esc(l.password)}</td></tr>
</table>
<p><b>M3U-Link:</b><br><a href="${esc(l.m3u)}">${esc(l.m3u)}</a></p>
<p><b>So geht's:</b> Öffnen Sie eine IPTV-App wie IBO Player Pro, IPTV Smarters oder TiviMate, wählen Sie „Xtream Codes“ und tragen Sie Server-URL, Benutzername und Passwort ein. Alternativ fügen Sie den M3U-Link ein.</p>
<p>Fragen zur Einrichtung? Antworten Sie einfach auf diese E-Mail, wir helfen gern.</p>
<p>Viel Spaß beim Testen!<br>Ihr Team von IPTV Welt Premium</p>
</div>`;

const contactHtml = (c) => `<p><b>Vorname:</b> ${esc(c.firstName)}<br><b>E-Mail:</b> ${esc(c.email)}<br>
<b>Telefon / WhatsApp:</b> ${esc(c.dial)} ${esc(c.phone)} (${esc(c.country)})</p>
<p><b>Notizen:</b><br>${esc(c.notes || "–").replace(/\n/g, "<br>")}</p>`;

export async function onRequestPost({ request, env }) {
  const { error, contact: c } = await readContact(request);
  if (error) return error;
  if (!env.TREX_API_KEY || !env.RESEND_API_KEY) return json({ error: "not_configured" }, 503);

  const to = env.TRIAL_TO || "kontakt@iptvweltpremium.de";
  const from = env.TRIAL_FROM || "IPTV Welt Premium <kontakt@iptvweltpremium.de>";
  const ip = request.headers.get("CF-Connecting-IP") || "";
  const keys = [`e:${c.email.toLowerCase()}`, `p:${c.dial}${c.phone}`, ip && `ip:${ip}`].filter(Boolean);

  // One trial per e-mail address, phone number and IP (only when the TRIAL_KV binding exists).
  if (env.TRIAL_KV) {
    const seen = await Promise.all(keys.map((k) => env.TRIAL_KV.get(k)));
    if (seen.some(Boolean)) return json({ error: "already_used" }, 409);
  }

  let line;
  try {
    line = await createDemo(env, c);
  } catch (err) {
    console.error(err);
    // Panel refused: hand the request to the team so nobody is lost.
    try {
      await sendMail(env, {
        from, to: [to], reply_to: c.email,
        subject: `Testanfrage MANUELL senden: ${c.firstName} (${c.country})`,
        html: `<h2>Automatischer Test fehlgeschlagen</h2><p>Das Panel hat keinen Testzugang erstellt. Bitte die Zugangsdaten manuell senden.</p>
<p><b>Fehler:</b> ${esc(err.message)}</p>${contactHtml(c)}`,
      });
      return json({ ok: true, manual: true });
    } catch (mailErr) {
      console.error(mailErr);
      return json({ error: "send_failed" }, 502);
    }
  }

  if (env.TRIAL_KV) {
    await Promise.all(keys.map((k) => env.TRIAL_KV.put(k, new Date().toISOString(), { expirationTtl: k.startsWith("ip:") ? DAY : 90 * DAY })));
  }

  const internal = {
    from, to: [to], reply_to: c.email,
    subject: `Neuer Test erstellt: ${c.firstName} (${c.country})`,
    html: `<h2>Neuer Testzugang erstellt</h2>
<p><b>Benutzername:</b> ${esc(line.username)}<br><b>Passwort:</b> ${esc(line.password)}<br><b>Server:</b> ${esc(line.server)}<br>
<b>Panel-ID:</b> ${esc(line.userId)} · <b>Paket:</b> ${esc(line.pack)}</p>${contactHtml(c)}`,
  };
  try {
    await sendMail(env, { from, to: [c.email], reply_to: to, subject: "Ihr kostenloser Testzugang – IPTV Welt Premium", html: customerHtml(c, line) });
  } catch (err) {
    console.error(err);
    internal.subject = `Test erstellt, E-Mail an Kunden FEHLGESCHLAGEN: ${c.firstName}`;
    internal.html = `<p><b>Die E-Mail an den Kunden konnte nicht gesendet werden. Bitte Zugangsdaten manuell senden.</b></p>${internal.html}`;
    await sendMail(env, internal).catch(console.error);
    return json({ ok: true, manual: true });
  }
  await sendMail(env, internal).catch(console.error);
  return json({ ok: true });
}
