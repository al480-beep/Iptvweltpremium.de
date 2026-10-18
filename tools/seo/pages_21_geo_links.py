# Verlinkung der Städte- und Regionenseiten von bestehenden Seiten aus
EXTEND = {
    "ratgeber": dict(into={"inhalte": '<div class="link-grid">{{card:iptv-staedte}}</div>'}),
    "iptv-deutschland": dict(related=["iptv-staedte", "iptv-sport", "iptv-international", "iptv-4k", "iptv-geraete", "kostenloser-test"]),
}
