// Cloudflare Pages Function: POST /api/trial
// Receives a free-trial request, emails it to the shop and sends the customer a confirmation.
//
// Environment variables (Cloudflare Pages → Settings → Variables and Secrets):
//   RESEND_API_KEY     required – API key from resend.com (domain iptvweltpremium.de verified there)
//   TRIAL_TO           optional – where requests go (default kontakt@iptvweltpremium.de)
//   TRIAL_FROM         optional – sender (default "IPTV Welt Premium <test@iptvweltpremium.de>")
//   TRIAL_WEBHOOK_URL  optional – also POST the request as JSON here (e.g. to automate credential creation)

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8" } });

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

async function sendMail(env, msg) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(msg),
  });
  if (!r.ok) throw new Error(`resend ${r.status}: ${await r.text()}`);
}

export async function onRequestPost({ request, env }) {
  let d;
  try {
    d = await request.json();
  } catch {
    return json({ error: "bad_request" }, 400);
  }

  // Bots fill the hidden "website" field; pretend success so they do not retry.
  if (d.website) return json({ ok: true });

  const firstName = String(d.firstName || "").trim().slice(0, 60);
  const email = String(d.email || "").trim().slice(0, 120);
  const country = String(d.country || "").trim().slice(0, 2).toUpperCase();
  const dial = String(d.dial || "").trim();
  const phone = String(d.phone || "").replace(/\D/g, "");
  const notes = String(d.notes || "").trim().slice(0, 1000);

  if (!firstName || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || !/^\+\d{1,4}$/.test(dial) || phone.length < 5 || phone.length > 15) {
    return json({ error: "invalid" }, 422);
  }
  if (!env.RESEND_API_KEY) return json({ error: "not_configured" }, 503);

  const to = env.TRIAL_TO || "kontakt@iptvweltpremium.de";
  const from = env.TRIAL_FROM || "IPTV Welt Premium <test@iptvweltpremium.de>";
  const fullPhone = `${dial} ${phone}`;
  const request_ = { firstName, email, country, phone: fullPhone, notes, receivedAt: new Date().toISOString() };

  try {
    await sendMail(env, {
      from,
      to: [to],
      reply_to: email,
      subject: `Neue Testanfrage: ${firstName} (${country})`,
      html: `<h2>Neue Testanfrage</h2>
<p><b>Vorname:</b> ${esc(firstName)}<br><b>E-Mail:</b> ${esc(email)}<br><b>Telefon:</b> ${esc(fullPhone)} (${esc(country)})</p>
<p><b>Notizen:</b><br>${esc(notes || "–").replace(/\n/g, "<br>")}</p>`,
    });
    await sendMail(env, {
      from,
      to: [email],
      reply_to: to,
      subject: "Ihr kostenloser Test bei IPTV Welt Premium",
      html: `<p>Hallo ${esc(firstName)},</p>
<p>vielen Dank für Ihre Anfrage! Ihre Testzugangsdaten erhalten Sie in Kürze per E-Mail. Bitte sehen Sie auch im Spam-Ordner nach.</p>
<p>Fragen? Antworten Sie einfach auf diese E-Mail.</p>
<p>Viele Grüße<br>Ihr Team von IPTV Welt Premium</p>`,
    });
    if (env.TRIAL_WEBHOOK_URL) {
      await fetch(env.TRIAL_WEBHOOK_URL, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(request_) });
    }
  } catch (err) {
    console.error(err);
    return json({ error: "send_failed" }, 502);
  }
  return json({ ok: true });
}
