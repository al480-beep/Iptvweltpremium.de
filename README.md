# iptvweltpremium.de

Static German landing page for IPTV Welt Premium. Plain HTML, CSS and JavaScript with no build step.

## Structure

- `index.html` – homepage
- `preise/index.html` – pricing page (device switch, plans, full price table)
- `kostenloser-test/index.html` – free trial page (first name, email, country code, phone, notes)
- `functions/api/trial.js` – Cloudflare Pages Function behind the free trial form. Creates a demo M3U line in the Trex activation panel (template "Germany", panel note `Trial / iptvweltpremium.de / email | phone`) and emails the logins to the customer through Resend, with a copy to `kontakt@`. Customers get the server `http://line.trxdnscloud.ru` (env `TREX_SERVER`) and an m3u link on that server. It also schedules a reminder with the price list at Resend, sent 12 hours before the 24-hour trial ends (`REMINDER_HOURS`, `TRIAL_HOURS`); no cron job is needed. If the panel refuses (e.g. no demo tickets left) the request is emailed to `kontakt@` for manual handling.
  - Required secrets in Cloudflare Pages (Settings → Variables and Secrets, Production): `TREX_API_KEY`, `RESEND_API_KEY`
  - Optional: `TREX_SERVER`, `TREX_TEMPLATE` (default `Germany`), `TREX_PACK` (fixed package id), `TREX_API_URL`, `TRIAL_HOURS`, `REMINDER_HOURS`, `TRIAL_TO`, `TRIAL_FROM`
  - Recommended: a KV namespace bound as `TRIAL_KV` (Settings → Bindings) so each e-mail, phone number and IP gets only one trial, and orders can show the earlier trial and cancel its reminder
  - The sending domain `iptvweltpremium.de` must be verified at resend.com
- `functions/api/order.js` – orders from `/checkout/`, emailed to `kontakt@` through Resend with the first line `Automation / iptvweltpremium.de / Trial <username> (or "kein Trial") / name / email / phone`. Cancels the customer's pending trial reminder.
- `functions/api/_emails.js` – the HTML e-mail templates and the price list used in the reminder (keep it in step with `PRICES` in `main.js`)
- If `/api/order` fails, the browser falls back to EmailJS (service, template and public key in `CONFIG.emailjs` in `assets/js/main.js`). Template variables: `site_name, plan, price, device, name, from_name, from_email, email, phone, country, message, time`
- `tools/sync_layout.py` – copies the shared header/footer from `index.html` to every page; run it after changing them (`python3 tools/sync_layout.py <new-version>` also bumps the CSS/JS `?v=`)
- Every page uses the same two buttons: **Kostenlos testen** → `/kostenloser-test/`, **Jetzt starten** → `/preise/`
- When `style.css` or `main.js` change, bump the `?v=` number (`python3 tools/sync_layout.py <n>`) so browsers load the new file
- `assets/css/style.css` – all styles
- `assets/js/main.js` – pricing calculator, price table, checkout, sliders, banners, animations
- `assets/img/` – hero slideshow and highlight artwork (original, free to use)
- `impressum.html`, `datenschutz.html` – legal pages (fill in the placeholders before going live)
- `.github/workflows/deploy.yml` – deploys to Cloudflare Pages on every push to `main`

## Settings to change

In `assets/js/main.js`, at the top:

- `CONFIG.whatsapp` – WhatsApp number in international format without `+` (e.g. `4915112345678`); currently a temporary placeholder
- `CONFIG.whatsappDisplay` – the number as shown on the page
- `CONFIG.email` – contact email (`kontakt@iptvweltpremium.de`)
- `REVIEWS` – real customer reviews; the reviews slider stays hidden while this list is empty
- `PRICES` – prices per number of devices and duration in months

## Deployment

**Option A – Cloudflare Git integration (current setup):** in Cloudflare Pages, connect this repository, set the production branch to `main`, leave the build command empty and set the output directory to `/`. Every push to `main` goes live.

**Option B – GitHub Actions:** add the secrets `CLOUDFLARE_API_TOKEN` (permission *Cloudflare Pages: Edit*) and `CLOUDFLARE_ACCOUNT_ID`, plus the repository variable `DEPLOY_WITH_ACTIONS=true`, under **Settings → Secrets and variables → Actions**. The workflow in `.github/workflows/deploy.yml` then deploys to the Pages project `iptvweltpremium` on every push to `main`. It is skipped while that variable is unset.

## Local preview

```sh
python3 -m http.server 8080
```
