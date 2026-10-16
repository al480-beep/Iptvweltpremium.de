// Cloudflare Pages Function: POST /api/trial – free trial requests. See _shared.js for configuration.
import { readContact, deliver, esc } from "./_shared.js";

export async function onRequestPost({ request, env }) {
  const { error, contact: c } = await readContact(request);
  if (error) return error;
  return deliver(env, {
    kind: "trial",
    contact: c,
    subject: `Neue Testanfrage: ${c.firstName} (${c.country})`,
    detailsHtml: "<h2>Neue Testanfrage</h2>",
    customerSubject: "Ihr kostenloser Test bei IPTV Welt Premium",
    customerHtml: `<p>Hallo ${esc(c.firstName)},</p>
<p>vielen Dank für Ihre Anfrage! Ihre Testzugangsdaten erhalten Sie in Kürze per E-Mail. Bitte sehen Sie auch im Spam-Ordner nach.</p>
<p>Fragen? Antworten Sie einfach auf diese E-Mail.</p>
<p>Viele Grüße<br>Ihr Team von IPTV Welt Premium</p>`,
  });
}
