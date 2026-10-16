# iptvweltpremium.de

Static German landing page for IPTV Welt Premium. Plain HTML, CSS and JavaScript with no build step.

## Structure

- `index.html` – homepage
- `preise/index.html` – pricing page (device switch, plans, full price table, order dialog)
- `kostenloser-test/index.html` – free trial page with request form
- Every page uses the same two buttons: **Kostenlos testen** → `/kostenloser-test/`, **Jetzt starten** → `/preise/`
- When `style.css` or `main.js` change, bump the `?v=` number in every page so browsers load the new file
- `assets/css/style.css` – all styles
- `assets/js/main.js` – pricing calculator, price table, order dialog, sliders, banners, animations
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
