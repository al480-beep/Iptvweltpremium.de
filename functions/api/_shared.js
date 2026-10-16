// Shared helpers for the form endpoints (/api/trial and /api/order).
// Files starting with "_" are not turned into routes by Cloudflare Pages.
//
// Environment variables (Cloudflare Pages → Settings → Variables and Secrets):
//   RESEND_API_KEY     required – API key from resend.com (domain iptvweltpremium.de verified there)
//   TRIAL_TO           optional – where requests go (default kontakt@iptvweltpremium.de)
//   TRIAL_FROM         optional – sender (default "IPTV Welt Premium <test@iptvweltpremium.de>")
//   TRIAL_WEBHOOK_URL  optional – also POST every request as JSON here (e.g. to automate sending logins)

export const PRICES = {
  1: { 1: 9, 3: 29, 6: 39, 12: 49 },
  2: { 1: 18, 3: 50, 6: 69, 12: 89 },
  3: { 1: 27, 3: 75, 6: 105, 12: 135 },
  4: { 1: 36, 3: 99, 6: 140, 12: 180 },
  5: { 1: 45, 3: 120, 6: 175, 12: 225 },
};
export const DURATION = { 1: "1 Monat", 3: "3 Monate", 6: "6 Monate", 12: "1 Jahr" };
export const devicesLabel = (d) => `${d} ${d === 1 ? "Gerät" : "Geräte"}`;

export const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8" } });

export const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

// Validates the contact fields every form shares. Returns { error } or { contact }.
export async function readContact(request) {
  let d;
  try {
    d = await request.json();
  } catch {
    return { error: json({ error: "bad_request" }, 400) };
  }
  // Bots fill the hidden "website" field; pretend success so they do not retry.
  if (d.website) return { error: json({ ok: true }) };

  const contact = {
    firstName: String(d.firstName || "").trim().slice(0, 60),
    email: String(d.email || "").trim().slice(0, 120),
    country: String(d.country || "").trim().slice(0, 2).toUpperCase(),
    dial: String(d.dial || "").trim(),
    phone: String(d.phone || "").replace(/\D/g, ""),
    notes: String(d.notes || "").trim().slice(0, 1000),
    devices: Number(d.devices),
    months: Number(d.months),
  };
  const c = contact;
  if (!c.firstName || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(c.email) || !/^\+\d{1,4}$/.test(c.dial) || c.phone.length < 5 || c.phone.length > 15) {
    return { error: json({ error: "invalid" }, 422) };
  }
  return { contact };
}

async function sendMail(env, msg) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(msg),
  });
  if (!r.ok) throw new Error(`resend ${r.status}: ${await r.text()}`);
}

// Sends the internal notification, the customer confirmation and the optional webhook.
export async function deliver(env, { kind, contact, subject, detailsHtml, customerSubject, customerHtml, extra = {} }) {
  if (!env.RESEND_API_KEY) return json({ error: "not_configured" }, 503);
  const to = env.TRIAL_TO || "kontakt@iptvweltpremium.de";
  const from = env.TRIAL_FROM || "IPTV Welt Premium <test@iptvweltpremium.de>";
  const c = contact;
  const phone = `${c.dial} ${c.phone}`;
  try {
    await sendMail(env, {
      from,
      to: [to],
      reply_to: c.email,
      subject,
      html: `${detailsHtml}
<p><b>Vorname:</b> ${esc(c.firstName)}<br><b>E-Mail:</b> ${esc(c.email)}<br><b>Telefon / WhatsApp:</b> ${esc(phone)} (${esc(c.country)})</p>
<p><b>Notizen:</b><br>${esc(c.notes || "–").replace(/\n/g, "<br>")}</p>`,
    });
    await sendMail(env, { from, to: [c.email], reply_to: to, subject: customerSubject, html: customerHtml });
    if (env.TRIAL_WEBHOOK_URL) {
      await fetch(env.TRIAL_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ kind, firstName: c.firstName, email: c.email, country: c.country, phone, notes: c.notes, ...extra, receivedAt: new Date().toISOString() }),
      });
    }
  } catch (err) {
    console.error(err);
    return json({ error: "send_failed" }, 502);
  }
  return json({ ok: true });
}
