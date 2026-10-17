// Cloudflare Pages Function: POST /api/order – order from /checkout/, emailed to kontakt@ through Resend.
//
// The mail starts with "Automation / iptvweltpremium.de / <trial> / name / email / phone", where <trial>
// is the username of the free trial this customer got earlier (looked up in TRIAL_KV) or "kein Trial".
// A pending trial reminder for the same customer is cancelled, so buyers do not get it.
// Uses RESEND_API_KEY, TRIAL_TO, TRIAL_FROM and the TRIAL_KV binding, like trial.js.
import { readContact, json, sendMail, cancelMail, mailFrom, mailTo, findTrial } from "./_shared.js";
import { PRICES, DURATION_LABEL, deviceLabel, berlinTime, internalMail } from "./_emails.js";

export async function onRequestPost({ request, env }) {
  const { error, contact: c, data } = await readContact(request);
  if (error) return error;
  if (!env.RESEND_API_KEY) return json({ error: "not_configured" }, 503);

  const devices = Number(data.devices);
  const months = Number(data.months);
  const price = PRICES[devices]?.[months];
  if (!price) return json({ error: "invalid" }, 422);

  const phone = `${c.dial}${c.phone}`;
  const trial = await findTrial(env, c.email, phone).catch((err) => (console.error(err), null));
  const trialLabel = trial ? `Trial ${trial.username || "(Datum " + String(trial.created).slice(0, 10) + ")"}` : "kein Trial";
  const headline = `Automation / iptvweltpremium.de / ${trialLabel} / ${c.firstName} / ${c.email} / ${phone}`;
  const plan = `${DURATION_LABEL[months]}, ${deviceLabel(devices)} – ${price} €${months === 12 ? " (inkl. IBO Player Pro Premium Abo)" : ""}`;

  let reminder = "";
  if (trial?.reminderId) {
    try {
      await cancelMail(env, trial.reminderId);
      reminder = "Test-Erinnerung storniert";
    } catch (err) {
      console.error(err);
      reminder = "Test-Erinnerung war schon versendet oder konnte nicht storniert werden";
    }
  }

  try {
    await sendMail(env, {
      from: mailFrom(env), to: [mailTo(env)], reply_to: c.email,
      subject: headline,
      html: internalMail(headline, [
        ["Paket", plan],
        ["Preis", `${price} €`],
        ["Vorname", c.firstName],
        ["E-Mail", c.email],
        ["Telefon / WhatsApp", `${c.dial} ${c.phone} (${c.country})`],
        ["Notizen", c.notes || "–"],
        ["Trial", trial ? `${trial.username || "–"} · erstellt ${berlinTime(new Date(trial.created))}` : "kein Testzugang über die Website"],
        ["Erinnerung", reminder],
        ["Eingegangen", berlinTime(new Date())],
      ]),
    });
  } catch (err) {
    console.error(err);
    return json({ error: "send_failed" }, 502);
  }
  return json({ ok: true });
}
