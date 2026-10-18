# Interne Verlinkung der neuen Anleitungen, Vergleiche und Geräte-/App-Seiten: Ringe unter Geschwistern plus thematische Links von bestehenden Seiten.
# Liest die related-Listen aus den anderen Seitenmodulen und hängt Links an; keine Seite verlinkt sich selbst.
import importlib.util, pathlib

HERE = pathlib.Path(__file__).resolve().parent
_rel, _order = {}, []
for f in sorted(HERE.glob("pages_*.py")):
    if f.stem >= "pages_40":
        continue
    spec = importlib.util.spec_from_file_location("x_" + f.stem, f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for p in getattr(mod, "PAGES", []):
        _rel[p["slug"]] = list(p.get("related", []))
    for slug, e in getattr(mod, "EXTEND", {}).items():
        if "related" in e:
            _rel[slug] = list(e["related"])

RINGS = [
    ["perfect-player", "ott-navigator", "televizo", "lazy-iptv", "sparkle-tv", "iptv-extreme", "gse-smart-iptv", "net-iptv", "duplex-iptv", "stb-emulator"],
    ["iptv-nvidia-shield", "iptv-google-tv-chromecast", "iptv-ps5-xbox", "iptv-philips-tv", "iptv-sony-bravia", "iptv-panasonic-tv", "iptv-hisense-tcl",
     "iptv-xiaomi-tv-box", "iptv-raspberry-pi", "iptv-ipad", "iptv-windows-pc", "iptv-linux", "iptv-enigma2-dreambox", "iptv-chromecast-airplay", "fire-tv-stick-vs-android-tv-box"],
    ["iptv-aufnehmen", "iptv-catchup-timeshift", "iptv-epg-einrichten", "iptv-vpn", "iptv-wlan-oder-lan", "iptv-router-einstellungen",
     "iptv-internet-geschwindigkeit", "iptv-mehrere-geraete", "iptv-kindersicherung", "iptv-favoriten-sortieren", "iptv-reise-ausland"],
    ["tivimate-vs-iptv-smarters-pro", "tivimate-vs-ibo-player", "iptv-smarters-pro-vs-xciptv", "kodi-vs-vlc-iptv", "smart-iptv-vs-ss-iptv", "m3u-vs-xtream-codes", "beste-iptv-player"],
    ["iptv-vs-satellit", "iptv-vs-kabel", "iptv-vs-streaming-abos", "iptv-vs-dvb-t2"],
]

# bestehende Seite -> neue Seiten, die thematisch dazugehören
FROM_EXISTING = {
    "iptv-hilfe": ["iptv-wlan-oder-lan", "iptv-router-einstellungen", "iptv-internet-geschwindigkeit"],
    "iptv-einrichten": ["iptv-epg-einrichten", "iptv-favoriten-sortieren", "m3u-vs-xtream-codes"],
    "iptv-stream": ["iptv-vpn", "iptv-reise-ausland", "iptv-internet-geschwindigkeit"],
    "tivimate": ["tivimate-vs-iptv-smarters-pro", "tivimate-vs-ibo-player", "iptv-aufnehmen"],
    "iptv-smarters-pro": ["tivimate-vs-iptv-smarters-pro", "iptv-smarters-pro-vs-xciptv", "iptv-kindersicherung"],
    "ibo-player": ["tivimate-vs-ibo-player", "duplex-iptv"],
    "xciptv": ["iptv-smarters-pro-vs-xciptv", "iptv-extreme"],
    "smart-iptv": ["smart-iptv-vs-ss-iptv", "net-iptv"],
    "ss-iptv": ["smart-iptv-vs-ss-iptv", "net-iptv"],
    "set-iptv": ["beste-iptv-player"],
    "kodi-iptv": ["kodi-vs-vlc-iptv", "iptv-raspberry-pi", "iptv-linux"],
    "vlc-iptv": ["kodi-vs-vlc-iptv", "iptv-windows-pc"],
    "xtream-codes": ["m3u-vs-xtream-codes", "iptv-epg-einrichten"],
    "m3u-playlist": ["m3u-vs-xtream-codes", "perfect-player"],
    "iptv-samsung-tv": ["net-iptv", "duplex-iptv"],
    "iptv-lg-tv": ["net-iptv", "duplex-iptv"],
    "iptv-smart-tv": ["iptv-philips-tv", "iptv-sony-bravia", "iptv-panasonic-tv", "iptv-hisense-tcl"],
    "iptv-android": ["iptv-nvidia-shield", "iptv-google-tv-chromecast", "iptv-xiaomi-tv-box", "ott-navigator", "televizo"],
    "iptv-apple-tv-iphone": ["gse-smart-iptv", "iptv-ipad", "iptv-chromecast-airplay"],
    "iptv-pc-mac": ["iptv-windows-pc", "iptv-linux", "iptv-raspberry-pi"],
    "mag-box": ["stb-emulator", "iptv-enigma2-dreambox"],
    "formuler": ["stb-emulator"],
    "iptv-receiver": ["iptv-enigma2-dreambox", "iptv-vs-satellit"],
    "iptv-box": ["fire-tv-stick-vs-android-tv-box", "iptv-xiaomi-tv-box", "sparkle-tv"],
    "iptv-fire-tv-stick": ["fire-tv-stick-vs-android-tv-box", "iptv-vpn", "iptv-ps5-xbox", "lazy-iptv"],
    "iptv-stick": ["fire-tv-stick-vs-android-tv-box", "iptv-nvidia-shield"],
    "was-ist-iptv": ["iptv-vs-satellit", "iptv-vs-kabel", "iptv-vs-streaming-abos", "iptv-vs-dvb-t2"],
    "iptv-telekom-vodafone": ["iptv-vs-kabel", "iptv-router-einstellungen"],
    "iptv-sport": ["iptv-vs-streaming-abos", "iptv-aufnehmen"],
    "iptv-filme-serien": ["iptv-vs-streaming-abos"],
    "iptv-4k": ["iptv-internet-geschwindigkeit", "iptv-nvidia-shield"],
    "iptv-apps": ["beste-iptv-player", "perfect-player"],
    "iptv-geraete": ["fire-tv-stick-vs-android-tv-box"],
    "iptv-anbieter-vergleich": ["beste-iptv-player", "iptv-vs-streaming-abos"],
    "iptv-russisch": ["iptv-georgien"],
    "iptv-ex-yu": ["iptv-georgien"],
    "iptv-albanisch": ["iptv-georgien"],
    "iptv-rumaenisch": ["iptv-georgien"],
    "iptv-international": ["iptv-filme-serien"],
    "iptv-sky": ["iptv-filme-serien"],
    "iptv-kaufen": ["iptv-mehrere-geraete"],
    "iptv-anbieter": ["iptv-vs-streaming-abos"],
}


NEW_LINKS = {
    "m3u-playlist": ["iptv-playlist-deutsch"], "iptv-deutschland": ["iptv-playlist-deutsch", "iptv-bundesliga"], "xtream-codes": ["iptv-playlist-deutsch", "iptv-account"],
    "iptv-4k": ["iptv-8k"], "iptv-internet-geschwindigkeit": ["iptv-8k"], "iptv-hilfe": ["iptv-account", "iptv-tester"],
    "iptv-einrichten": ["iptv-account", "iptv-tester"], "tivimate": ["tivimate-apple-tv"], "iptv-apple-tv-iphone": ["tivimate-apple-tv", "iptv-smarters-pro-iphone"],
    "iptv-ipad": ["tivimate-apple-tv", "iptv-smarters-pro-iphone"], "iptv-pc-mac": ["iptv-macbook", "iptv-smarters-pro-windows"], "vlc-iptv": ["iptv-macbook", "iptv-tester"],
    "iptv-windows-pc": ["iptv-macbook", "iptv-smarters-pro-windows"], "iptv-sport": ["iptv-bundesliga"], "iptv-aufnehmen": ["iptv-bundesliga"],
    "iptv-wlan-oder-lan": ["iptv-bundesliga"], "iptv-kaufen": ["iptv-abo"], "iptv-mehrere-geraete": ["iptv-abo"], "iptv-anbieter-vergleich": ["iptv-tester"],
    "iptv-smarters-pro": ["iptv-smarters-pro-windows", "iptv-smarters-pro-iphone"], "kodi-iptv": ["kodi-fire-tv-stick"], "iptv-fire-tv-stick": ["kodi-fire-tv-stick"],
    "iptv-raspberry-pi": ["kodi-fire-tv-stick"], "iptv-geraete": ["iptv-macbook"],
}
for _k, _v in NEW_LINKS.items():
    FROM_EXISTING[_k] = FROM_EXISTING.get(_k, []) + _v


def _add(slug, extra, cap=9):
    cur = _rel.get(slug, [])
    for x in extra:
        if x != slug and x not in cur and len(cur) < cap:
            cur = cur + [x]
    _rel[slug] = cur


for ring in RINGS:
    n = len(ring)
    for i, s in enumerate(ring):
        _add(s, [ring[(i + 1) % n], ring[(i + 2) % n]])
for s, extra in FROM_EXISTING.items():
    _add(s, extra, cap=12)

EXTEND = {s: dict(related=_rel[s]) for ring in RINGS for s in ring}
EXTEND.update({s: dict(related=_rel[s]) for s in FROM_EXISTING})
