// Cloudflare Pages Function: POST /api/order – plan orders from /checkout/. See _shared.js for configuration.
import { readContact, deliver, esc, json, PRICES, DURATION, devicesLabel } from "./_shared.js";

export async function onRequestPost({ request, env }) {
  const { error, contact: c } = await readContact(request);
  if (error) return error;
  const price = PRICES[c.devices]?.[c.months];
  if (!price) return json({ error: "invalid_plan" }, 422);
  const plan = `${DURATION[c.months]}, ${devicesLabel(c.devices)}`;
  const bonus = c.months === 12 ? " inkl. IBO Player Pro Premium Abo" : "";
  return deliver(env, {
    kind: "order",
    contact: c,
    extra: { plan, devices: c.devices, months: c.months, price },
    subject: `Neue Bestellung: ${plan} – ${price} € (${c.firstName})`,
    detailsHtml: `<h2>Neue Bestellung</h2><p><b>Paket:</b> ${esc(plan)}${esc(bonus)}<br><b>Preis:</b> ${price} €</p>`,
    customerSubject: "Ihre Bestellung bei IPTV Welt Premium",
    customerHtml: `<p>Hallo ${esc(c.firstName)},</p>
<p>vielen Dank für Ihre Bestellung: <b>${esc(plan)}${esc(bonus)}</b> für <b>${price} €</b>.</p>
<p>Wir melden uns in Kürze per E-Mail oder WhatsApp mit Ihren Zugangsdaten. Bitte sehen Sie auch im Spam-Ordner nach.</p>
<p>Fragen? Antworten Sie einfach auf diese E-Mail.</p>
<p>Viele Grüße<br>Ihr Team von IPTV Welt Premium</p>`,
  });
}
