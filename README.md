# iptvweltpremium.de

Static German landing page for IPTV Welt Premium. Plain HTML, CSS and JavaScript with no build step.

## Structure

- `index.html` – main page (hero, features, pricing calculator, steps, devices, FAQ, contact)
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

Add two repository secrets under **Settings → Secrets and variables → Actions**:

- `CLOUDFLARE_API_TOKEN` – a token with the *Cloudflare Pages: Edit* permission
- `CLOUDFLARE_ACCOUNT_ID` – your Cloudflare account ID

Every push to `main` then publishes the site to the Cloudflare Pages project `iptvweltpremium`. Connect the custom domain `iptvweltpremium.de` once in the Cloudflare dashboard under **Workers & Pages → iptvweltpremium → Custom domains**.

## Local preview

```sh
python3 -m http.server 8080
```
