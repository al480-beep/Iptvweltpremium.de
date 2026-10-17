#!/usr/bin/env python3
"""Build the SEO landing and guide pages from tools/seo/pages_*.py.

Every page is written to /<slug>/index.html with the shared header/footer from index.html,
breadcrumbs, a table of contents, FAQ (HTML + FAQPage JSON-LD), related links and the CTA box.
It also rewrites sitemap.xml and prints a keyword coverage report.
Run from the repository root after editing a page module or the header/footer:  python3 tools/seo/build.py
"""
import html, importlib.util, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SEO = pathlib.Path(__file__).resolve().parent
SITE = "https://iptvweltpremium.de"
BRAND = "IPTV Welt Premium"
UPDATED = "2026-10-17"          # change only when the content really changes
CSS_V = "12"
OG_IMAGE = f"{SITE}/assets/img/og-image.jpg"

# Pages that already exist outside the generator (for breadcrumbs and related links)
STATIC = {
    "": {"nav": "Startseite", "card": "Premium IPTV mit +50.000 Live-Kanälen und 4K.", "title": BRAND},
    "preise": {"nav": "Preise", "card": "Alle Pakete für 1 bis 5 Geräte, ab 4,08 € im Monat.", "title": "IPTV Preise"},
    "kostenloser-test": {"nav": "Kostenloser Test", "card": "IPTV 24 Stunden gratis testen, ohne Zahlungsdaten.", "title": "IPTV kostenlos testen"},
}


def load_pages():
    pages = []
    for f in sorted(SEO.glob("pages_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pages.extend(mod.PAGES)
    slugs = [p["slug"] for p in pages]
    dupes = {s for s in slugs if slugs.count(s) > 1}
    if dupes:
        sys.exit(f"duplicate slugs: {dupes}")
    return {p["slug"]: p for p in pages}


def layout(master, name):
    m = re.search(rf"<!-- layout:{name} -->.*?<!-- /layout:{name} -->", master, re.S)
    return m.group(0)


def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def url(slug):
    return f"{SITE}/{slug}/" if slug else f"{SITE}/"


def href(slug):
    return f"/{slug}/" if slug else "/"


def info(slug, pages):
    return pages.get(slug) or STATIC[slug]


def chain(page, pages):
    out, cur = [], page
    while cur.get("parent") is not None:
        cur = info(cur["parent"], pages)
        out.insert(0, cur)
    return out


def slug_of(p, pages):
    for k, v in {**STATIC, **pages}.items():
        if v is p:
            return k
    return p.get("slug", "")


def card(slug, pages):
    if slug not in pages and slug not in STATIC:
        print(f"  ! missing card target {slug}")
        return ""
    p = info(slug, pages)
    return (f'<a class="card" href="{href(slug)}"><h3>{p["nav"]}</h3><p>{p["card"]}</p>'
            f'<span>Weiterlesen →</span></a>')


def build_toc(body):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if len(items) < 3:
        return ""
    lis = "".join(f'<li><a href="#{i}">{strip_tags(t)}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-label="Inhaltsverzeichnis"><b>Inhalt</b><ol>{lis}</ol></nav>'


def render(page, pages, master, plans_block):
    slug = page["slug"]
    crumbs = chain(page, pages)
    title, desc = page["title"], page["desc"]
    body = page["body"]
    if "{{children}}" in body:
        kids = [s for s, p in pages.items() if p.get("parent") == slug]
        body = body.replace("{{children}}", '<div class="link-grid">' + "".join(card(s, pages) for s in kids) + "</div>")
    body = re.sub(r"\{\{card:([a-z0-9-]*)\}\}", lambda m: card(m.group(1), pages), body)

    # Breadcrumb
    bc_items = [(slug_of(c, pages), c["nav"]) for c in crumbs] + [(slug, page["nav"])]
    bc_html = "".join(
        (f'<li><a href="{href(s)}">{n}</a></li>' if i < len(bc_items) - 1 else f'<li aria-current="page">{n}</li>')
        for i, (s, n) in enumerate(bc_items))
    # FAQ
    faq = page.get("faq", [])
    faq_html = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}<i aria-hidden="true"></i></summary><div><p>{a}</p></div></details>'
        for i, (q, a) in enumerate(faq))
    # JSON-LD
    org = {"@type": "Organization", "@id": f"{SITE}/#org", "name": BRAND, "url": f"{SITE}/",
           "logo": f"{SITE}/assets/img/logo-560.png", "email": "kontakt@iptvweltpremium.de",
           "contactPoint": {"@type": "ContactPoint", "contactType": "customer support",
                            "email": "kontakt@iptvweltpremium.de", "availableLanguage": ["de", "en"]}}
    kind = page.get("schema", "Article")
    main = {"@type": kind, "@id": url(slug) + "#main", "url": url(slug), "name": strip_tags(page["h1"]),
            "headline": strip_tags(page["h1"])[:110], "description": desc, "inLanguage": "de-DE",
            "image": OG_IMAGE, "datePublished": page.get("published", UPDATED), "dateModified": UPDATED,
            "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"},
            "isPartOf": {"@id": f"{SITE}/#website"}, "breadcrumb": {"@id": url(slug) + "#breadcrumb"}}
    if kind == "CollectionPage":
        for k in ("headline", "author"):
            main.pop(k)
    if page.get("about"):
        main["about"] = [{"@type": "Thing", "name": a} for a in page["about"]]
    graph = [org, {"@type": "WebSite", "@id": f"{SITE}/#website", "name": BRAND, "url": f"{SITE}/",
                   "inLanguage": "de-DE", "publisher": {"@id": f"{SITE}/#org"}}, main,
             {"@type": "BreadcrumbList", "@id": url(slug) + "#breadcrumb", "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "name": n, "item": url(s)} for i, (s, n) in enumerate(
                     [("", "Startseite")] + [b for b in bc_items if b[0] != ""])]}]
    if faq:
        graph.append({"@type": "FAQPage", "@id": url(slug) + "#faq", "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faq]})
    if page.get("offer"):
        graph.append({"@type": "Service", "@id": url(slug) + "#service", "name": "IPTV Welt Premium Abo",
                      "serviceType": "IPTV-Abonnement", "provider": {"@id": f"{SITE}/#org"},
                      "areaServed": [{"@type": "Country", "name": n} for n in ("Deutschland", "Österreich", "Schweiz")],
                      "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "9", "highPrice": "225",
                                 "offerCount": "20", "url": f"{SITE}/preise/"}})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

    plans = ""
    if page.get("plans"):
        plans = f'''
  <section id="preise" class="pricing">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Pakete &amp; Preise</span>
        <h2 class="display">{page.get("plans_title", 'Ein Abo. <span class="grad-text">Alle Inhalte.</span>')}</h2>
        <p>Einmal zahlen, sofort schauen. Keine automatische Verlängerung, kein Vertrag.</p>
      </div>
      {plans_block}
    </div>
  </section>'''
    related = page.get("related", [])
    related_html = ""
    if related:
        related_html = f'''
  <section class="related">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Weiterlesen</span>
        <h2 class="display">Passende <span class="grad-text">Ratgeber</span></h2>
      </div>
      <div class="link-grid">{"".join(card(s, pages) for s in related)}</div>
    </div>
  </section>'''
    faq_sec = ""
    if faq:
        faq_sec = f'''
  <section id="faq">
    <div class="container faq-wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Häufige Fragen</span>
        <h2 class="display">{page.get("faq_title", 'Fragen &amp; <span class="grad-text">Antworten</span>')}</h2>
        <p>Ihre Frage ist nicht dabei? Schreiben Sie uns per <a href="#" data-wa>WhatsApp</a>, wir antworten schnell.</p>
      </div>
      <div class="faq reveal d1">{faq_html}</div>
    </div>
  </section>'''
    answer = f'<div class="answer-box"><b>Kurz gesagt</b><p>{page["answer"]}</p></div>' if page.get("answer") else ""
    date_de = ".".join(reversed(UPDATED.split("-")))
    og_type = "website" if kind in ("CollectionPage", "WebPage") else "article"
    e = html.escape
    out = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url(slug)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#07070d">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(page.get("og_title", title))}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(slug)}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BRAND}: IPTV mit Live-TV, Filmen und Serien">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(page.get("og_title", title))}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/logo-560.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_V}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

{layout(master, "top")}

<main>
  <section class="page-hero">
    <div class="page-hero-bg" aria-hidden="true" style="background-image:url('/assets/img/{page.get("bg", "photo-3.jpg")}')"></div>
    <div class="container">
      <nav aria-label="Brotkrumen"><ol class="breadcrumb">{bc_html}</ol></nav>
      <span class="eyebrow">{page["eyebrow"]}</span>
      <h1 class="display">{page["h1"]}</h1>
      <p class="lead">{page["lead"]}</p>
      <div class="hero-actions">
        <a href="/preise/" class="btn btn-primary">Jetzt starten <svg><use href="#i-arrow"/></svg></a>
        <a href="/kostenloser-test/" class="btn btn-ghost">Kostenlos testen</a>
      </div>
      <p class="page-meta">Zuletzt aktualisiert: {date_de} · Redaktion {BRAND}</p>
    </div>
  </section>

  <section class="article">
    <div class="container">
      {answer}
      {build_toc(body)}
      <div class="prose">
{body}
      </div>
    </div>
  </section>
{plans}{faq_sec}{related_html}
  <section class="cta-band-wrap">
    <div class="container">
      <div class="cta-box reveal">
        <span class="eyebrow">Kostenloser Test</span>
        <h2 class="display">Erst testen. <span class="grad-text">Dann entscheiden.</span></h2>
        <p>{page.get("cta", "Prüfen Sie Bildqualität, Senderauswahl und Stabilität kostenlos auf Ihrem eigenen Gerät.")}</p>
        <div class="cta-pair" style="justify-content:center"><a href="/preise/" class="btn btn-primary">Jetzt starten <svg><use href="#i-arrow"/></svg></a><a href="/kostenloser-test/" class="btn btn-ghost">Kostenlos testen</a></div>
        <div class="cta-perks">
          <span><svg><use href="#i-check-c"/></svg>Voller Zugriff im Testzeitraum</span>
          <span><svg><use href="#i-check-c"/></svg>Keine Zahlungsdaten nötig</span>
          <span><svg><use href="#i-check-c"/></svg>Persönliche Einrichtungshilfe</span>
        </div>
      </div>
    </div>
  </section>
</main>

{layout(master, "bottom")}
<script src="/assets/js/main.js?v={CSS_V}" defer></script>
</body>
</html>
'''
    return out


def check(page, pages):
    errs = []
    t = page["title"]
    if not 30 <= len(t) <= 65:
        errs.append(f"title length {len(t)}")
    if not 110 <= len(page["desc"]) <= 165:
        errs.append(f"desc length {len(page['desc'])}")
    for s in page.get("related", []) + ([page["parent"]] if page.get("parent") else []):
        if s not in pages and s not in STATIC:
            errs.append(f"unknown link {s}")
    for s in re.findall(r'href="/([a-z0-9-]+)/"', page["body"]):
        if s not in pages and s not in STATIC and s not in ("checkout",):
            errs.append(f"unknown body link /{s}/")
    return errs


def main():
    pages = load_pages()
    master = (ROOT / "index.html").read_text(encoding="utf-8")
    plans_block = re.search(r"<!-- plans:start -->.*?<!-- plans:end -->", master, re.S).group(0)
    problems = 0
    for slug, page in pages.items():
        for err in check(page, pages):
            print(f"  ! {slug}: {err}")
            problems += 1
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(page, pages, master, plans_block), encoding="utf-8")
    # sitemap
    urls = [("", "1.0"), ("preise", "0.9"), ("kostenloser-test", "0.9")]
    urls += [(s, p.get("priority", "0.7")) for s, p in pages.items()]
    lines = [f"  <url><loc>{url(s)}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority></url>" for s, pr in urls]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "\n".join(lines) + "\n</urlset>\n", encoding="utf-8")
    print(f"built {len(pages)} pages, {problems} warnings")
    return pages


if __name__ == "__main__":
    main()
