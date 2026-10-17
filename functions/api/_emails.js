// E-mail templates for the trial and order endpoints (German, inline styles so every mail client renders them).
import { esc } from "./_shared.js";

export const SITE = "https://iptvweltpremium.de";

export const PRICES = {
  1: { 1: 9, 3: 29, 6: 39, 12: 49 },
  2: { 1: 18, 3: 50, 6: 69, 12: 89 },
  3: { 1: 27, 3: 75, 6: 105, 12: 135 },
  4: { 1: 36, 3: 99, 6: 140, 12: 180 },
  5: { 1: 45, 3: 120, 6: 175, 12: 225 },
};
export const DURATION_LABEL = { 1: "1 Monat", 3: "3 Monate", 6: "6 Monate", 12: "1 Jahr" };
export const deviceLabel = (d) => `${d} ${d === 1 ? "Gerät" : "Geräte"}`;

export const berlinTime = (date) =>
  date.toLocaleString("de-DE", { timeZone: "Europe/Berlin", day: "2-digit", month: "2-digit", year: "numeric", hour: "2-digit", minute: "2-digit" }) + " Uhr";

const FONT = "font-family:'Segoe UI',Helvetica,Arial,sans-serif";

// Common frame: dark header with logo, white card, footer.
const layout = (preheader, body) => `<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"></head>
<body style="margin:0;padding:0;background:#eef1f7">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">${esc(preheader)}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#eef1f7"><tr><td align="center" style="padding:28px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;background:#ffffff;border-radius:18px;overflow:hidden;box-shadow:0 10px 30px rgba(7,7,13,.08)">
<tr><td align="center" style="background:#07070d;background-image:linear-gradient(120deg,#0b1a3a 0%,#07070d 60%);padding:30px 24px 26px">
<a href="${SITE}/" style="text-decoration:none"><img src="${SITE}/assets/img/logo-560.png" width="240" alt="IPTV Welt Premium" style="display:block;width:240px;max-width:80%;height:auto;border:0;color:#ffffff;${FONT};font-size:22px;font-weight:bold"></a>
</td></tr>
<tr><td style="height:4px;background:#1e7bff;background-image:linear-gradient(90deg,#22d3ee,#1e7bff,#4f46e5);font-size:0;line-height:0">&nbsp;</td></tr>
<tr><td style="padding:34px 32px 30px;${FONT};font-size:15px;line-height:1.65;color:#1b1d29">
${body}
</td></tr>
<tr><td style="background:#f6f8fc;padding:22px 32px;${FONT};font-size:12px;line-height:1.6;color:#7c7f94;text-align:center">
Fragen? Antworten Sie einfach auf diese E-Mail, wir helfen Ihnen gern.<br>
<a href="${SITE}/" style="color:#1e6bff;text-decoration:none">iptvweltpremium.de</a> · <a href="${SITE}/impressum.html" style="color:#7c7f94">Impressum</a> · <a href="${SITE}/datenschutz.html" style="color:#7c7f94">Datenschutz</a>
</td></tr>
</table>
</td></tr></table>
</body></html>`;

const button = (href, label) => `<table role="presentation" cellpadding="0" cellspacing="0" align="center" style="margin:26px auto 8px"><tr>
<td align="center" style="border-radius:999px;background:#1e7bff;background-image:linear-gradient(120deg,#22d3ee 0%,#1e7bff 50%,#4f46e5 100%)">
<a href="${href}" style="display:inline-block;padding:14px 34px;${FONT};font-size:16px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:999px">${label}</a>
</td></tr></table>`;

const credRow = (label, value, last) => `<tr>
<td style="padding:13px 18px;${last ? "" : "border-bottom:1px solid #dfe6f3;"}${FONT};font-size:13px;color:#5d6178;white-space:nowrap;width:96px">${label}</td>
<td style="padding:13px 18px;${last ? "" : "border-bottom:1px solid #dfe6f3;"}font-family:Consolas,'Courier New',monospace;font-size:15px;font-weight:bold;color:#0b1a3a;word-break:break-all">${value}</td>
</tr>`;

const step = (n, title, text) => `<tr>
<td valign="top" style="padding:0 14px 16px 0;width:34px"><div style="width:30px;height:30px;line-height:30px;border-radius:50%;background:#e6f0ff;color:#1e6bff;text-align:center;${FONT};font-weight:bold;font-size:14px">${n}</div></td>
<td valign="top" style="padding:3px 0 16px;${FONT};font-size:14px;line-height:1.6;color:#33364a"><b style="color:#1b1d29">${title}</b><br>${text}</td>
</tr>`;

export const trialCustomerMail = (c, l, expires) => {
  const body = `<h1 style="margin:0 0 6px;${FONT};font-size:26px;line-height:1.25;color:#0b1a3a">Hallo ${esc(c.firstName)}! 👋</h1>
<p style="margin:0 0 18px;font-size:16px;color:#33364a">Schön, dass Sie IPTV Welt Premium ausprobieren. Ihr <b>kostenloser Testzugang ist ab sofort aktiv</b>, Sie können direkt loslegen.</p>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 6px;background:#f3f7ff;border:1px solid #dfe6f3;border-radius:14px">
<tr><td colspan="2" style="padding:14px 18px 4px;${FONT};font-size:12px;font-weight:bold;letter-spacing:.08em;text-transform:uppercase;color:#1e6bff">Ihre Zugangsdaten</td></tr>
${credRow("Server-URL", `<a href="${esc(l.server)}" style="color:#0b1a3a;text-decoration:none">${esc(l.server)}</a>`)}
${credRow("Benutzername", esc(l.username))}
${credRow("Passwort", esc(l.password), true)}
</table>
<p style="margin:0 0 22px;font-size:13px;color:#5d6178">⏳ Gültig bis <b>${esc(berlinTime(expires))}</b> (deutsche Zeit)</p>

<p style="margin:0 0 6px;font-size:13px;font-weight:bold;color:#1b1d29">M3U-Link (für Apps ohne Xtream-Login):</p>
<p style="margin:0 0 26px;padding:12px 14px;background:#f6f8fc;border:1px dashed #c9d3e6;border-radius:10px;font-family:Consolas,'Courier New',monospace;font-size:12.5px;line-height:1.5;word-break:break-all"><a href="${esc(l.m3u)}" style="color:#1e6bff;text-decoration:none">${esc(l.m3u)}</a></p>

<h2 style="margin:0 0 14px;${FONT};font-size:18px;color:#0b1a3a">In 3 Schritten zum Fernsehen</h2>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
${step(1, "App installieren", "Zum Beispiel IBO Player Pro, IPTV Smarters Pro oder TiviMate auf Smart-TV, Fire TV Stick, Handy oder PC.")}
${step(2, "„Xtream Codes“ wählen", "Server-URL, Benutzername und Passwort von oben eintragen. Alternativ den M3U-Link einfügen.")}
${step(3, "Zurücklehnen und genießen", "Sender, Filme und Serien laden automatisch. Fertig!")}
</table>

<p style="margin:8px 0 0;padding:14px 16px;background:#fff8e6;border-radius:10px;font-size:14px;color:#5b4a12">💬 <b>Brauchen Sie Hilfe bei der Einrichtung?</b> Antworten Sie einfach auf diese E-Mail und nennen Sie Ihr Gerät, wir melden uns schnell.</p>
${button(`${SITE}/preise/`, "Pakete &amp; Preise ansehen")}
<p style="margin:22px 0 0;color:#33364a">Viel Spaß beim Testen!<br><b>Ihr Team von IPTV Welt Premium</b></p>`;
  return layout(`Ihre Zugangsdaten sind da – Benutzername ${l.username}`, body);
};

const priceBlock = (d) => {
  const rows = Object.keys(PRICES[d]).map((m, k, all) => {
    const best = m === "12";
    return `<tr><td style="padding:9px 14px;${k < all.length - 1 ? "border-bottom:1px solid #e8edf6;" : ""}${FONT};font-size:14px;color:#33364a">${DURATION_LABEL[m]}${best ? ' <span style="display:inline-block;margin-left:4px;padding:1px 7px;border-radius:999px;background:#e6f0ff;color:#1e6bff;font-size:11px;font-weight:bold">Bestpreis</span>' : ""}</td>
<td align="right" style="padding:9px 14px;${k < all.length - 1 ? "border-bottom:1px solid #e8edf6;" : ""}${FONT};font-size:15px;font-weight:bold;white-space:nowrap"><a href="${SITE}/checkout/?geraete=${d}&amp;laufzeit=${m}" style="color:#0b1a3a;text-decoration:none">${PRICES[d][m]} €</a></td></tr>`;
  }).join("");
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 14px;border:1px solid #dfe6f3;border-radius:12px;overflow:hidden">
<tr><td colspan="2" style="padding:10px 14px;background:#0b1a3a;${FONT};font-size:14px;font-weight:bold;color:#ffffff">⭐ ${deviceLabel(Number(d))} ⭐</td></tr>
${rows}</table>`;
};

export const reminderMail = (firstName, expires) => {
  const body = `<h1 style="margin:0 0 6px;${FONT};font-size:24px;line-height:1.25;color:#0b1a3a">Hallo ${esc(firstName)}, Ihr Test endet bald ⏳</h1>
<p style="margin:0 0 14px;font-size:16px;color:#33364a">Ihr kostenloser Testzugang läuft am <b>${esc(berlinTime(expires))}</b> ab. Wir hoffen, Ihnen gefällt das Programm!</p>
<p style="margin:0 0 22px;font-size:15px;color:#33364a">Damit Sie ohne Unterbrechung weiterschauen können, wählen Sie jetzt einfach Ihr Abo. Klicken Sie auf einen Preis, um direkt zu bestellen:</p>
${Object.keys(PRICES).map(priceBlock).join("")}
<p style="margin:6px 0 0;font-size:13px;color:#5d6178">✔ Sofortige Freischaltung · ✔ Beim Jahresabo inklusive IBO Player Pro Premium · ✔ Persönlicher Support</p>
${button(`${SITE}/preise/`, "Jetzt Abo wählen")}
<p style="margin:22px 0 0;color:#33364a">Fragen zu den Paketen? Antworten Sie einfach auf diese E-Mail.<br><br>Herzliche Grüße<br><b>Ihr Team von IPTV Welt Premium</b></p>`;
  return layout("Ihr Testzugang läuft bald ab – jetzt Abo wählen und weiterschauen", body);
};

// Internal mails to kontakt@ start with one summary line, e.g. "Trial / iptvweltpremium.de / Anna / anna@x.de / +49151...".
export const internalMail = (headline, rows) => `<div style="${FONT};font-size:15px;line-height:1.6;color:#111">
<p style="font-size:17px;font-weight:bold;margin:0 0 14px">${esc(headline)}</p>
<table cellpadding="6" style="border-collapse:collapse">${rows
  .filter(([, v]) => v !== undefined && v !== "")
  .map(([k, v]) => `<tr><td style="color:#555;vertical-align:top"><b>${esc(k)}</b></td><td>${esc(v).replace(/\n/g, "<br>")}</td></tr>`)
  .join("")}</table></div>`;
