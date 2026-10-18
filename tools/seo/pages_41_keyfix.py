# Suchbegriffe mit Volumen, die in den neuen Seiten noch nicht wörtlich vorkamen: je ein natürlicher Satz im passenden Abschnitt
EXTEND = {
    "beste-iptv-player": dict(into={"kriterien": '<p>Suchanfragen wie „bester IPTV Player“ oder „beste IPTV App“ liefern oft Bestenlisten mit bezahlten Platzierungen. Entscheidend sind Ihr Gerät, die Bedienung und die Pflege der App, nicht die Position in einer Liste.</p>'}),
    "iptv-sony-bravia": dict(into={"anleitung": '<p>Wer nach „IPTV Sony Bravia“ sucht, will meist wissen, ob ein Sony-Fernseher ohne Zusatzgerät IPTV abspielt. Mit Google TV ja, bei Modellen ohne App-Store hilft ein Stick am HDMI-Anschluss.</p>'}),
    "iptv-hisense-tcl": dict(into={"tabelle": '<p>Die Suche nach „IPTV Hisense“ führt häufig zu VIDAA-Modellen. Dort entscheidet das App-Angebot im Store, bei Google-TV-Modellen sind die gängigen IPTV-Apps verfügbar.</p>'}),
    "iptv-nvidia-shield": dict(into={"vorteile": '<p>„IPTV Nvidia Shield“ ist eine häufige Suche, weil das Gerät als sehr stabil gilt. Der Grund ist die Kombination aus LAN-Anschluss, viel Rechenleistung und dem Play Store.</p>'}),
    "iptv-enigma2-dreambox": dict(into={"prinzip": '<p>„IPTV Enigma2“ beschreibt keine App, sondern eine Methode: Die Playlist wird in eine Senderliste des Receivers umgewandelt.</p>'}),
    "iptv-ipad": dict(into={"anleitung": '<p>Wer „IPTV iPad“ sucht, braucht keine Zusatzgeräte: Die App aus dem App Store genügt, für den Fernseher kommt AirPlay dazu.</p>'}),
    "iptv-google-tv-chromecast": dict(into={"unterschied": '<p>Bei der Suche nach „IPTV Chromecast“ lohnt der Blick auf das Modell: Nur Geräte mit Google TV führen Apps direkt aus, ältere Modelle empfangen nur Übertragungen.</p>'}),
}

# Hauptbegriff je Seite: steht wörtlich im Titel oder in der H1
PRIMARY = {
    "tivimate-vs-iptv-smarters-pro": "tivimate oder iptv smarters pro", "tivimate-vs-ibo-player": "tivimate oder ibo player",
    "iptv-smarters-pro-vs-xciptv": "iptv smarters pro oder xciptv", "kodi-vs-vlc-iptv": "kodi oder vlc für iptv",
    "beste-iptv-player": "beste iptv player", "iptv-vs-streaming-abos": "iptv oder streaming-abos",
    "iptv-nvidia-shield": "iptv auf der nvidia shield", "iptv-ps5-xbox": "iptv auf ps5 und xbox",
    "iptv-philips-tv": "iptv auf philips-fernseher", "iptv-sony-bravia": "iptv auf sony bravia",
    "iptv-panasonic-tv": "iptv auf panasonic-fernseher", "iptv-hisense-tcl": "iptv auf hisense und tcl",
    "iptv-xiaomi-tv-box": "iptv auf der xiaomi tv box", "iptv-ipad": "iptv auf dem ipad", "iptv-linux": "iptv unter linux",
    "iptv-enigma2-dreambox": "iptv auf enigma2", "iptv-chromecast-airplay": "iptv übertragen",
    "iptv-wlan-oder-lan": "iptv per wlan oder lan", "iptv-router-einstellungen": "router für iptv einstellen",
    "iptv-internet-geschwindigkeit": "wie schnell muss das internet für iptv sein", "iptv-mehrere-geraete": "iptv auf mehreren geräten",
    "iptv-kindersicherung": "kindersicherung bei iptv", "iptv-reise-ausland": "iptv im urlaub und im ausland",
}
for _s, _k in PRIMARY.items():
    EXTEND.setdefault(_s, {})["kw_add"] = [_k]
EXTEND.setdefault("iptv-google-tv-chromecast", {})["kw_add"] = ["iptv chromecast", "iptv auf google tv"]
EXTEND.setdefault("iptv-raspberry-pi", {})["kw_remove"] = ["libreelec iptv"]

# Ein Suchbegriff gehört genau einer Seite: die neue, spezialisierte Seite übernimmt ihn von der allgemeineren
for _s, _k in {"iptv-kaufen": ["iptv abo", "iptv account"], "iptv-4k": ["iptv 8k"], "iptv-apps": ["iptv extreme"],
               "iptv-apple-tv-iphone": ["iptv smarters pro iphone", "tivimate apple tv"], "iptv-windows-pc": ["iptv pc"],
               "iptv-einrichten": ["iptv tester"], "m3u-playlist": ["iptv playlist deutsch"], "iptv-sport": ["iptv bundesliga"],
               "iptv-stick": ["iptv chromecast"]}.items():
    EXTEND.setdefault(_s, {})["kw_remove"] = _k
for _s, _k in {"iptv-raspberry-pi": "iptv auf dem raspberry pi", "iptv-macbook": "iptv auf dem macbook", "kodi-fire-tv-stick": "kodi auf dem fire tv stick"}.items():
    EXTEND.setdefault(_s, {}).setdefault("kw_add", []).append(_k)
EXTEND.setdefault("iptv-windows-pc", {}).setdefault("kw_add", []).append("iptv auf windows")
