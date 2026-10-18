# Städte- und Regionenseiten (Cluster "Geo"): Hub, Bundesländer und Städte aus den Datendateien geo_*.py.
# Jede Seite hat eigene Texte zu Fernsehen, Sport, Internet und Wohnsituation vor Ort; nur die 4 Einrichtungsschritte sind gemeinsam.
import html, re, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from geo_cities_1 import CITIES as C1
from geo_cities_2 import CITIES as C2
from geo_cities_3 import CITIES as C3
from geo_cities_4 import CITIES as C4
from geo_cities_5 import CITIES as C5, WOHNEN as W5, ALLTAG as A5
from geo_cities_6 import CITIES as C6, WOHNEN as W6, ALLTAG as A6
from geo_cities_7 import CITIES as C7, WOHNEN as W7, ALLTAG as A7
from geo_states import STATES
from geo_wohnen import WOHNEN
from geo_alltag import ALLTAG

CITIES = C1 + C2 + C3 + C4 + C5 + C6 + C7
WOHNEN = {**WOHNEN, **W5, **W6, **W7}
ALLTAG = {**ALLTAG, **A5, **A6, **A7}
CITY = {c["slug"]: c for c in CITIES}
STATE = {s["slug"]: s for s in STATES}
HUB = "iptv-staedte"

LINKS = [
    ("IPTV International", "/iptv-international/"), ("IPTV Deutschland", "/iptv-deutschland/"), ("IPTV Sport", "/iptv-sport/"),
    ("IPTV in 4K", "/iptv-4k/"), ("IPTV Stream", "/iptv-stream/"), ("IPTV Hilfe", "/iptv-hilfe/"),
    ("Preisseite", "/preise/"), ("kostenlosen Test", "/kostenloser-test/"), ("Anleitung zum Fire TV Stick", "/iptv-fire-tv-stick/"),
    ("IBO Player", "/ibo-player/"), ("Anleitungen für Samsung und LG", "/iptv-geraete/"),
]


def esc(t):
    return html.escape(t, quote=False)


def linkify(t, used=None):
    t = esc(t)
    for phrase, href in LINKS:
        if phrase in t and (used is None or href not in used):
            t = t.replace(phrase, f'<a href="{href}">{phrase}</a>', 1)
            if used is not None:
                used.add(href)
    return t


def short(name):
    return re.sub(r" \(.*\)| am Main| im Breisgau", "", name)


def pid(slug):
    return "iptv-" + slug


def exists(slug):
    return slug in CITY or slug in STATE


STEPS = '''<ol>
  <li><strong>Test anfordern:</strong> der <a href="/kostenloser-test/">kostenlose 24-Stunden-Test</a> zeigt Bild und Senderauswahl.</li>
  <li><strong>Gerät und App wählen:</strong> <a href="/iptv-geraete/">IPTV Geräte</a> und <a href="/iptv-apps/">IPTV Apps</a>.</li>
  <li><strong>Zugang eintragen:</strong> <a href="/xtream-codes/">Xtream Codes</a> oder <a href="/m3u-playlist/">M3U Playlist</a>.</li>
  <li><strong>Paket wählen:</strong> <a href="/preise/">Preise</a>, ohne Vertrag.</li>
</ol>'''


def city_page(c):
    n, s = c["name"], short(c["name"])
    st = STATE.get(c["state"]) if c["state"] else None
    parent = pid(c["state"]) if st else HUB
    region = c.get("region") or st["name"]
    used = {"/kostenloser-test/"}
    near = [pid(x) for x in c["nearby"] if exists(x)]
    related = ([parent] if st else []) + [HUB] + near[:2] + ["iptv-deutschland", "kostenloser-test"]
    body = f'''
<h2 id="fernsehen">Fernsehen in {esc(n)}: Regionales und Heimatsender</h2>
<p>{linkify(c["tv"], used)}</p>

<h2 id="sport">Sport und Veranstaltungen in {esc(n)} live</h2>
<p>{linkify(c["sport"], used)}</p>

<h2 id="technik">Internet und Technik in {esc(n)}</h2>
<p>{linkify(c["net"], used)}</p>

<h2 id="wohnen">Wohnen in {esc(n)}: so richten Sie IPTV zu Hause ein</h2>
<p>{linkify(WOHNEN[c["slug"]], used)}</p>
<p>{linkify(c["tip"], used)}</p>

<h2 id="alltag">Termine und Alltag in {esc(n)}: was das für IPTV bedeutet</h2>
<p>{linkify(ALLTAG[c["slug"]], used)}</p>

<h2 id="schritte">IPTV in {esc(n)} starten: 4 Schritte</h2>
{STEPS}
'''
    faq = [(esc(q), linkify(a)) for q, a in c["faqs"]]
    faq.append((f"Kann ich IPTV in {esc(n)} kostenlos testen?",
                f"Ja. Mit dem <a href=\"/kostenloser-test/\">kostenlosen 24-Stunden-Test</a> prüfen Sie in {esc(n)} Bild, Senderauswahl und Stabilität auf Ihrem eigenen Anschluss, ohne Zahlungsdaten. Danach wählen Sie Laufzeit und Geräteanzahl ab 4,08 € im Monat."))
    title = f"IPTV {s}: {c['tag']}"
    desc = f"IPTV in {n}: Fernsehen per Internet mit deutschen Sendern, Sport und Heimatsendern. Tipps zu Anschluss und Geräten. 24 Stunden gratis testen."
    return dict(
        slug=pid(c["slug"]), parent=parent, nav=f"IPTV {s}", priority="0.6",
        card=f"IPTV in {n}: {c['tag']}.",
        kw=[f"iptv {s.lower()}", f"iptv {s.lower()} kaufen", f"iptv anbieter {s.lower()}"],
        title=title, desc=desc, eyebrow=f"IPTV in {esc(region)}",
        h1=f'IPTV in {esc(n)}: <span class="grad-text">Live-TV, Sport und Heimat</span>',
        lead=esc(c["lead"]),
        answer=(f"IPTV Welt Premium läuft in {esc(n)} über Ihren vorhandenen Internetanschluss, ohne Satellitenschüssel und ohne Kabelvertrag, "
                f"auf bis zu 5 Geräten gleichzeitig. Besonders gefragt: {esc(c['tag'])}. Ab 4,08 € im Monat im Jahresabo, vorher 24 Stunden kostenlos testen."),
        about=[n], body=body, faq=faq, related=related,
        cta=f"Prüfen Sie in {esc(n)} Bildqualität, Senderauswahl und Stabilität kostenlos auf Ihrem eigenen Gerät.",
    )


def state_page(st):
    n = st["name"]
    kids = [c for c in CITIES if c["state"] == st["slug"]]
    cards = "".join("{{card:%s}}" % pid(c["slug"]) for c in kids)
    nb = [pid(x) for x in st["neighbors"] if x in STATE]
    nb += [pid(x) for x in st["neighbors"] if x in CITY]
    used = {"/kostenloser-test/"}
    body = f'''
<h2 id="fernsehen">Fernsehen in {esc(n)}: Regionales und Heimatsender</h2>
<p>{linkify(st["tv"], used)}</p>

<h2 id="sport">Sport und Veranstaltungen in {esc(n)}</h2>
<p>{linkify(st["sport"], used)}</p>

<h2 id="technik">Internet und Technik in {esc(n)}</h2>
<p>{linkify(st["net"], used)}</p>

<h2 id="alltag">Termine und Alltag in {esc(n)}: was das für IPTV bedeutet</h2>
<p>{linkify(ALLTAG[st["slug"]], used)}</p>

<h2 id="staedte">IPTV in den Städten von {esc(n)}</h2>
<p>{esc(n)} hat {esc(st["pop"])} Einwohner und die Landeshauptstadt {esc(st["cap"])}. Für diese Städte finden Sie eigene Seiten mit Fernsehen, Sport, Internet und Wohnsituation vor Ort:</p>
<div class="link-grid">{cards}</div>

<h2 id="schritte">IPTV in {esc(n)} starten: 4 Schritte</h2>
{STEPS}
'''
    faq = [(esc(q), linkify(a)) for q, a in st["faqs"]]
    faq.append((f"Kann ich IPTV in {esc(n)} kostenlos testen?",
                f"Ja. Der <a href=\"/kostenloser-test/\">kostenlose 24-Stunden-Test</a> funktioniert überall in {esc(n)}, wo Ihr Internetanschluss stabil läuft. Danach wählen Sie Laufzeit und Geräteanzahl ab 4,08 € im Monat."))
    related = [HUB] + nb[:4] + ["kostenloser-test"]
    return dict(
        slug=pid(st["slug"]), parent=HUB, nav=f"IPTV {n}", priority="0.7",
        card=f"IPTV in {n}: {st['tag']}.",
        kw=[f"iptv {n.lower()}", f"iptv {st['slug'].replace('-', ' ')}"] if st["slug"] != n.lower() else [f"iptv {n.lower()}"],
        title=f"IPTV {n}: {st['tag']}", desc=f"IPTV in {n}: Fernsehen per Internet mit regionalen Sendern, Sport und Heimatsendern. Tipps zu Anschluss und Städten. 24 Stunden gratis testen.",
        eyebrow="Bundesland", h1=f'IPTV in {esc(n)}: <span class="grad-text">Fernsehen per Internet</span>',
        lead=esc(st["lead"]),
        answer=(f"IPTV Welt Premium läuft überall in {esc(n)}, wo ein stabiler Internetanschluss liegt, auf Smart-TV, Stick, Box, Handy und PC. "
                f"Besonders gefragt: {esc(st['tag'])}. Ab 4,08 € im Monat im Jahresabo, vorher 24 Stunden kostenlos testen."),
        about=[n], body=body, faq=faq, related=related,
        cta=f"Prüfen Sie in {esc(n)} Bildqualität, Senderauswahl und Stabilität kostenlos auf Ihrem eigenen Gerät.",
    )


def hub_page():
    sections = []
    for st in STATES:
        kids = [c for c in CITIES if c["state"] == st["slug"]]
        cards = "{{card:%s}}" % pid(st["slug"]) + "".join("{{card:%s}}" % pid(c["slug"]) for c in kids)
        sections.append(f'<h2 id="{st["slug"]}">{esc(st["name"])}</h2>\n<div class="link-grid">{cards}</div>')
    states_html = "\n\n".join(sections)
    free = [c for c in CITIES if c["state"] is None]
    free_cards = "".join("{{card:%s}}" % pid(c["slug"]) for c in free)
    body = f'''
<h2 id="so-funktioniert">Ein Abo, überall in Deutschland</h2>
<p>IPTV Welt Premium kommt über das Internet ins Haus. Deshalb ist das Angebot in jeder Stadt dasselbe: deutsche Sender samt dritter Programme, Sport, Filme, Serien und internationale Ländergruppen. Was sich unterscheidet, sind die regionalen Programme, der Sport vor Ort, die Anbieter und die Wohnsituation. Auf den folgenden Seiten finden Sie genau diese Unterschiede für Ihre Stadt und Ihr Bundesland.</p>
<p>Egal wo Sie wohnen: Prüfen Sie Bild und Senderauswahl zuerst mit dem <a href="/kostenloser-test/">kostenlosen 24-Stunden-Test</a>. Die Pakete mit Preisen für 1 bis 5 Geräte stehen auf der <a href="/preise/">Preisseite</a>.</p>

<h2 id="stadtstaaten">Stadtstaaten: Berlin, Hamburg und Bremen</h2>
<div class="link-grid">{free_cards}</div>

{states_html}

<h2 id="hinweise">Was für alle Städte gilt</h2>
<ul>
  <li><strong>Internetgeschwindigkeit:</strong> rund 16 Mbit/s für HD, etwa 30 Mbit/s für 4K, wie im Ratgeber <a href="/iptv-stream/">IPTV Stream</a> erklärt.</li>
  <li><strong>Geräte:</strong> Smart-TV, Stick, Box, Handy oder PC, siehe <a href="/iptv-geraete/">IPTV Geräte</a>.</li>
  <li><strong>Heimatsender:</strong> Ländergruppen für Balkan, Albanien, Rumänien, Georgien und mehr unter <a href="/iptv-international/">IPTV International</a>.</li>
  <li><strong>Probleme:</strong> Lösungen für Ruckeln und Login-Fehler in der <a href="/iptv-hilfe/">IPTV Hilfe</a>.</li>
</ul>
'''
    faq = [("Ist IPTV Welt Premium in jeder Stadt verfügbar?", "Ja, überall dort, wo Sie einen stabilen Internetanschluss haben. Das Angebot kommt über das Internet, nicht über Kabel oder Satellit."),
           ("Warum gibt es Seiten für einzelne Städte?", "Weil sich regionale Programme, Sport, Internetanbieter und Wohnsituation unterscheiden. Auf den Stadtseiten stehen genau diese lokalen Hinweise."),
           ("Fehlt meine Stadt?", "Schreiben Sie unserem Support. Das Angebot läuft trotzdem auch dort, die Anleitungen im Ratgeber gelten überall."),
           ("Kann ich IPTV im Urlaub in einer anderen Stadt nutzen?", "Ja, mit einem Stick oder Handy und stabiler Verbindung, solange die erlaubte Geräteanzahl eingehalten wird.")]
    return dict(
        slug=HUB, parent="", nav="IPTV Städte & Regionen", priority="0.8", schema="CollectionPage",
        card="IPTV für Ihre Stadt und Ihr Bundesland: lokale Sender, Sport und Anschlusstipps.",
        kw=["iptv städte", "iptv regionen", "iptv bundesländer", "iptv in meiner stadt"],
        title="IPTV in Deutschland: Städte, Regionen und Bundesländer",
        desc="IPTV für Ihre Stadt: regionale Sender, Sport vor Ort, Anschluss und Geräte für über 50 Städte und alle Bundesländer. Jetzt 24 Stunden gratis testen.",
        eyebrow="Städte & Regionen", h1='IPTV in Deutschland: <span class="grad-text">Ihre Stadt, Ihr Bundesland</span>',
        lead="Ein Abo für ganz Deutschland, mit den Besonderheiten Ihrer Region: Hier finden Sie Seiten für Bundesländer und Städte mit lokalen Hinweisen zu Fernsehen, Sport und Internet.",
        answer="IPTV Welt Premium funktioniert in ganz Deutschland über jeden stabilen Internetanschluss. Auf den Seiten für Städte und Bundesländer finden Sie regionale Programme, den Sport vor Ort und Tipps zu Anschluss und Geräten.",
        body=body, faq=faq, related=["iptv-deutschland", "iptv-international", "iptv-geraete", "ratgeber", "kostenloser-test", "preise"],
    )


PAGES = [hub_page()] + [state_page(s) for s in STATES] + [city_page(c) for c in CITIES]
