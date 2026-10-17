# Zweite Runde: mehr Tiefe für Kauf-, Ratgeber-, Inhalts- und Vergleichsseiten.
# "into" ergänzt einen bestehenden Abschnitt (per h2-id), "body" hängt nur wirklich neue Abschnitte an.
EXTEND = {

"iptv-kaufen": dict(
    into={
        "kosten": '''<p>Wer gezielt nach IPTV 12 Monate, IPTV 12 months oder IPTV M3U 1 Jahr sucht, bekommt mit dem Jahresabo genau das: einen M3U-Link und Xtream-Daten, die 12 Monate gültig sind und danach einfach enden.</p>''',
        "worauf-achten": '''<p>Vorsicht bei IPTV Deals, IPTV Sale oder IPTV Promotions mit Countdown und bei Lifetime IPTV: „Lifetime“ meint in der Praxis die Lebensdauer des Anbieters. Unsere Preise sind fest und stehen offen auf der <a href="/preise/">Preisseite</a>; das günstigste IPTV Angebot ist bei uns immer das Jahresabo. Prüfen Sie jeden IPTV Shop, auch wenn die IPTV Angebote verlockend klingen, mit den Punkten oben.</p>''',
        "m3u-oder-xtream": '''<p>Wenn Sie IPTV M3U kaufen, bekommen Sie also beides. Nicht verwechseln mit „Smart IPTV kaufen“: Smart IPTV ist nur ein Player, dessen Freischaltung Sie beim App-Entwickler bezahlen, siehe <a href="/smart-iptv/">Smart IPTV</a>.</p>''',
        "zahlung": '''<p>Ihr IPTV Account besteht aus Benutzername, Passwort und Serveradresse. Ob IPTV Paysafecard für Ihre Bestellung möglich ist, klären wir gern direkt mit Ihnen.</p>''',
    },
    body='''
<h2 id="english">Buy IPTV in Germany (in English)</h2>
<p>Looking to buy IPTV for Germany? An IPTV subscription from IPTV Welt Premium includes German and international channels plus a large on-demand library in HD and 4K. To subscribe, pick a plan on the prices page and enter your name, e-mail and phone number; we send your IPTV account within 5 to 15 minutes. Every IPTV premium subscription runs without automatic renewal, so an IP TV subscription for 12 months simply ends after 12 months. Whether you search for IPTV buy, IPTV sub or IPTV subscribe, the order form is the same, and you can start with the free 24-hour trial. Many people also search for generic “IPTV com” sites: before ordering anywhere, check for a free trial, reachable support and clear prices.</p>
''',
    faq=[
        ("Can I buy an IPTV subscription in English?", "Yes. Our support answers in German and English. Choose a plan on the prices page or start with the free 24-hour trial."),
    ],
),

"iptv-deutschland": dict(
    kw_remove=["iptv stream", "ip tv streaming", "stream iptv", "iptv live", "iptv tv", "iptv ip",
               "world iptv", "worldwide iptv", "euro iptv", "iptv one", "my iptv"],
    into={
        "sender": '''<p>Wer nach „IPTV alle Sender“ sucht, findet hier also die gewohnten Programme. Die IPTV Sender aus anderen Ländern stehen in eigenen Gruppen, siehe <a href="/iptv-international/">IPTV International</a>.</p>''',
        "live-streamen": '''<p>So funktioniert Deutsch IPTV bzw. Deutschland IPTV im Alltag: deutscher Programmführer, deutsche App-Oberfläche und deutscher Support, ohne Receiver und ohne Vertrag. Wie die Technik dahinter funktioniert, erklärt <a href="/iptv-stream/">IPTV Stream</a>.</p>''',
    },
    body='''
<h2 id="english">IPTV Germany for expats (in English)</h2>
<p>Living in Germany and looking for German IPTV with English support? Germany IPTV from IPTV Welt Premium gives you the German channels, international channels and films in one plan. IPTV German channels work on Fire TV, smart TVs, phones and PCs, and our support answers in English too. Every IPTV Germany plan can be tested free for 24 hours first.</p>
''',
    faq=[
        ("Is there English support for German IPTV?", "Yes, our support answers in German and English via WhatsApp and e-mail, 24/7."),
    ],
),

"iptv-international": dict(
    kw_remove=["iptv ge", "iptv ge imedi", "imedi tv live iptv ge", "iptv ge live", "iptv ge rustavi2"],
    kw_add=["world iptv", "worldwide iptv", "euro iptv"],
    title="IPTV International: England, BBC, Balkan & Worldwide",
    desc="IPTV International: Heimatsender aus dem Balkan, Albanien, Rumänien, Georgien, Großbritannien und vielen weiteren Ländern neben deutschen Sendern in einer App.",
    replace=[('<p>Georgische Familien in Deutschland suchen häufig nach Imedi TV, Rustavi 2 oder dem öffentlich-rechtlichen Sender 1TV. Die Sender selbst bieten teils Livestreams auf ihren Websites an. In unserer Playlist finden Sie georgische Programme, soweit verfügbar, in der internationalen Gruppe.</p>',
              '<p>Georgische Familien in Deutschland suchen häufig nach Imedi TV, Rustavi 2 oder dem öffentlich-rechtlichen Sender 1TV. Alles dazu lesen Sie auf der Seite <a href="/iptv-georgien/">IPTV Georgien</a>.</p>')],
    into={
        "uk": '''<p>IPTV England ist bei Briten in Deutschland und bei Fans der Premier League gefragt. Für IPTV BBC gilt: Die linearen Sender schauen Sie per IPTV mit Programmführer, den iPlayer nur in Großbritannien.</p>''',
        "weitere": '''<p>Worldwide IPTV heißt bei uns nicht, dass Sie für jedes Land ein eigenes Paket kaufen: World IPTV mit allen Ländergruppen ist im selben Abo enthalten, von Euro IPTV mit Sendern aus Italien, Spanien, Frankreich, Polen und den Niederlanden bis zu Programmen aus Osteuropa und dem Kaukasus.</p>''',
    },
),

"iptv-anbieter-vergleich": dict(
    into={
        "warum-selbst": '''<p>Ob Sie nach „best IPTV“, „bester IPTV“ oder vertippt „bes IPTV“ suchen: Den einen Sieger für alle gibt es nicht. Für Fußballfans zählt die Stabilität am Samstag, für Familien die Zahl der Geräte, für Heimatsender die Ländergruppen.</p>''',
        "reddit-foren": '''<p>Das gilt für jede Suche nach „best IPTV Reddit“, „Reddit best IPTV“ oder „best IPTV provider Reddit“, für IPTV Reddit-Threads allgemein, für jedes IPTV Anbieter Forum und für IPTV Trustpilot-Profile. Threads zu „IPTV Smarters Reddit“ oder „TiviMate Reddit“ sind dagegen oft hilfreich, weil es dort um Software geht, nicht um Anbieter.</p>''',
    },
),

"iptv-anbieter": dict(
    into={
        "checkliste": '''<p>Mit dieser Liste finden Sie den besten IPTV Anbieter für Ihren Alltag, auch wenn Sie den „bester IPTV Anbieter“-Listen im Netz nicht trauen.</p>''',
        "warnsignale": '''<p>Eine seriöse IPTV Site oder IPTV Website hat dagegen ein Impressum, offene Preise, einen Test ohne Zahlungsdaten und antwortet auf Fragen schnell.</p>''',
        "vergleichen": '''<p>Ein IPTV Stream Anbieter liefert Sender als Livestream über das Internet, wie in <a href="/iptv-stream/">IPTV Stream</a> erklärt. Wer einen IPTV Anbieter Sky sucht, meint oft Sky selbst; Sky bietet mit Sky Stream eine eigene Lösung mit Sky-Abo, mehr unter <a href="/iptv-sky/">IPTV Sky</a>.</p>''',
    },
    body='''
<h2 id="english">IPTV providers: a short guide in English</h2>
<p>Internet Protocol TV providers deliver live TV over your internet connection instead of cable or satellite. When choosing the best IPTV provider, look for a free trial, 24/7 support and no automatic renewal. Among IPTV providers, these three points separate reliable services from short-lived ones; IPTV Welt Premium offers all three.</p>
''',
),

"iptv-anbieter-alternativen": dict(
    kw_add=["extreme iptv", "upiptv", "pandar tv", "iptv one", "dlta 4k"],
    into={
        "namen": '''<p>Dazu kommen viele Schreibweisen, und nicht jede Website mit dem Namen gehört zum Dienst. Häufig gesucht werden zum Beispiel auch Fox TV IPTV bzw. IPTV Fox, GoldIPTV (nicht zu verwechseln mit Golden IPTV), MU3 IPTV, Quzu IPTV, Rapid Swiss IPTV, IPTVPortal, Pandar TV, UPIPTV, IPTV One und DLTA 4K. Hinter manchen Namen steckt kein Endkunden-Abo, sondern Software für Betreiber. Auch zu diesen Namen machen wir keine Aussagen über Qualität oder Seriosität.</p>''',
    },
),

"iptv-sport": dict(
    into={
        "sportarten": '''<p>Wer gezielt nach IPTV Eurosport, IPTV ESPN oder IPTV beIN Sport sucht, findet diese Sender in der Gruppe Sport international, soweit verfügbar.</p>''',
        "fussball": '''<p>Für IPTV Champions League gilt: Dienstag und Mittwoch früh einschalten, dann sind die Server weniger belastet. IPTV Premier League-Spiele finden Sie in der Gruppe UK und Sport international, samstags meist ab 16 Uhr deutscher Zeit. Wer international nach „IPTV soccer“ sucht, meint dieselben Ligen. Für IPTV World Cup und EM empfehlen wir, frühzeitig zu testen und nicht erst am Spieltag.</p>''',
        "formel1": '''<p>Für IPTV F1 lohnt sich außerdem eine Favoriten-Gruppe mit allen Motorsport-Sendern.</p>''',
        "nba-ufc": '''<p>IPTV NBA und IPTV UFC finden Sie in der Gruppe Sport international; die Anstoßzeiten zeigt das EPG in deutscher Zeit.</p>''',
    },
),

"iptv-sky": dict(
    into={
        "sky-q-iptv": '''<p>Wer nach „Sky IPTV Box“, „Sky Q IPTV Box Preis“ oder „Sky Q IPTV Box UHD“ sucht, findet die verbindlichen Antworten deshalb nur bei Sky: Der Preis hängt vom gewählten Sky-Abo ab, UHD vom gebuchten Paket.</p>''',
        "sport-alternative": '''<p>Viele suchen nach „IPTV Sky Sport“, „Sky Sport IPTV“ oder „IPTV Sky Deutschland“. Offiziell gibt es Sky-Sender nur über Sky selbst; wir machen keine Aussagen über einzelne Sky-Sender in unserer Playlist.</p>''',
    },
),

"iptv-filme-serien": dict(
    into={
        "vod": '''<p>IPTV VOD ist also der Teil des Abos, den Sie wie eine Mediathek nutzen. Die IPTV Series-Bibliothek ist nach Staffeln und Folgen sortiert, mit Fortsetzen-Funktion.</p>''',
        "streamingdienste": '''<p>Zu Suchen wie „IPTV HBO“, „IPTV HBO Max“, „IPTV Discovery Plus“ oder „IPTV Pluto TV“: Diese Dienste haben eigene Apps und Abos. Wir machen keine Aussagen darüber, ob bestimmte Titel dieser Dienste in unserer Bibliothek sind; was enthalten ist, sehen Sie im <a href="/kostenloser-test/">kostenlosen Test</a>.</p>''',
    },
),

"iptv-ex-yu": dict(
    into={
        "dobrodosli": '''<p lang="sr-Latn">IPTV televizija bez satelitske antene: kanali iz Srbije, Hrvatske, Bosne i Hercegovine, Crne Gore i Sjeverne Makedonije, zajedno sa njemačkim programom u jednoj aplikaciji.</p>''',
        "kanali": '''<p lang="sr-Latn">IPTV kanali su sortirani po državama, sa EPG vodičem.</p>''',
        "paketi": '''<p lang="sr-Latn">IPTV paketi i IPTV ponuda: jedan paket sadrži sve kanale. IPTV cena za jedan uređaj: 9 € za mjesec ili 49 € za 12 mjeseci, bez automatskog produženja.</p>''',
        "programi": '''<p lang="sr-Latn">IPTV programi sa EPG vodičem i Catch-Up funkcijom, gdje je dostupno.</p>''',
    },
),

"iptv-albanisch": dict(
    into={
        "mire-se-vini": '''<p>Ob Sie nach „Alb Kanal IPTV“ oder „Albkanale IPTV“ suchen: Gemeint ist genau diese Gruppe.</p>''',
        "kanale": '''<p>IPTV Iliria ist eine eigenständige Plattform; wir haben nichts damit zu tun und machen keine Aussagen über deren Angebot.</p>''',
        "live": '''<p>Für IPTV Shqip live nutzen Sie am besten die Favoritenliste, damit Ihre Lieblingssender ganz oben stehen.</p>''',
    },
),

"iptv-rumaenisch": dict(
    into={
        "canale": '''<p lang="ro">Canale romanesti IPTV pentru familiile din Germania: știri, emisiuni și seriale din România, alături de programele germane într-o singură aplicație. Puteți testa gratuit 24 de ore, fără date de plată.</p>''',
    },
    body='''
<h2 id="tipps">Tipps für ruckelfreien Empfang</h2>
<p>Abends, wenn in Rumänien die Hauptnachrichten laufen, sind die Netze stark ausgelastet. Verbinden Sie den Fernseher möglichst per LAN-Kabel und wählen Sie bei schwacher Leitung die HD- statt der 4K-Variante eines Senders. Ein Abo reicht für bis zu 5 Geräte gleichzeitig, die Preise stehen auf der <a href="/preise/">Preisseite</a>. Weitere Tipps finden Sie in der <a href="/iptv-hilfe/">IPTV Hilfe</a>.</p>
''',
),

"iptv-russisch": dict(
    into={
        "angebot": '''<p>Unter „RU IPTV“ oder „IPTV russische TV“ finden Sie bei uns diese Gruppe, soweit die Programme in der EU verbreitet werden dürfen (siehe unten).</p>''',
    },
),

"was-ist-iptv": dict(
    into={
        "definition": '''<p>Ob Sie es IP Television, IPTV Television oder Television IPTV nennen: gemeint ist immer dieses Prinzip.</p>''',
        "vergleich": '''<p>Wer nach „Sat IP TV“ sucht, meint meist genau diese SAT>IP-Technik.</p>''',
        "arten": '''<p>Daneben gibt es IPTV Web-Angebote im Browser, die meist weniger stabil sind als Apps. Das IPTV Programm (in anderen Sprachen „IPTV programa“) läuft heute fast immer in einer App.</p>''',
        "voraussetzungen": '''<p>Früher brauchten Sie für Fernsehen und Internet zwei Anschlüsse. Heute reicht einer: Television and internet kommen über dieselbe Leitung.</p>''',
    },
    body='''
<h2 id="english">What is Internet Protocol Television?</h2>
<p>What is Internet Protocol Television? IPTV delivers TV channels over an IP network, the same technology that powers the internet, instead of cable, satellite or antenna. You watch live channels with a programme guide and on-demand films in an app on your TV, stick, phone or computer. All you need is a stable internet connection and an IPTV subscription.</p>
''',
),

"iptv-einrichten": dict(
    into={
        "schritt-4": '''<p>Diese Setting IPTV-Punkte machen in jeder App den größten Unterschied.</p>''',
        "test": '''<p>Für den schnellen Technik-Check reicht ein einfacher IPTV Tester: VLC am Computer, M3U-Adresse als Netzwerkstream öffnen. Erscheint die Senderliste, sind die Zugangsdaten korrekt. Apps, die sich IPTV Tester oder Checker nennen, machen im Prinzip dasselbe; geben Sie Ihre Daten aber nur in Apps aus offiziellen Stores ein.</p>''',
        "support": '''<p>Unser IPTV Customer Service hilft bei Zugang, Sendern und Einrichtung; für Fehler in einer App ist deren Entwickler zuständig.</p>''',
    },
),

"xtream-codes": dict(
    into={
        "aufbau": '''<p>Eine IPTV Linie (englisch „line“) ist also Ihr persönlicher Zugang, mit fester Laufzeit und Geräteanzahl. Beim Testzugang spricht man von einer Testline.</p>''',
        "apps": '''<p>Xtream IPTV bezeichnet heute meist genau diesen Login mit Server, Benutzername und Passwort.</p>''',
        "m3u-aus-xtream": '''<p>So wird aus dem Xtream IPTV-Zugang ein Xtream IPTV M3U-Link, beide führen zur selben Senderliste.</p>''',
        "server": '''<p>Wie viele IPTV Servers ein Anbieter betreibt, sehen Sie von außen nicht. Messbar ist nur die Stabilität bei Ihnen zu Hause.</p>''',
        "reseller": '''<p>Zur Einordnung: Ein Reseller for IPTV kauft Zugänge bei einem Betreiber ein und verkauft sie unter eigenem Namen weiter. Für Endkunden zählt vor allem, wer bei Problemen erreichbar ist.</p>''',
    },
),

"iptv-telekom-vodafone": dict(
    into={
        "telekom": '''<p>Telekom IP TV bzw. Magenta IPTV ist dabei fest an den Anschluss oder das Kundenkonto gebunden.</p>''',
        "vodafone": '''<p>Vodafone IP TV bzw. Vodafone IPTV läuft je nach Anschluss über GigaTV-App oder Box. Wer IPTV Vodafone-seitig schon nutzt, kann unser Angebot zusätzlich testen.</p>''',
        "1und1-o2": '''<p>O2 IPTV, also das Fernsehangebot von O2, läuft über eine App.</p>''',
    },
),

"iptv-4k": dict(
    kw_remove=["dlta 4k"],
    into={
        "geraete": '''<p>Als IPTV Box 4K eignen sich vor allem Nvidia Shield, Homatics und Ugoos; als IPTV Receiver 4K Linux-Geräte wie die MAG 420 oder aktuelle Formuler-Modelle. Details unter <a href="/iptv-box/">IPTV Box</a> und <a href="/mag-box/">MAG Box</a>.</p>''',
        "premium": '''<p>Viele Anbieter nennen sich „IP TV Premium“. Echtes IPTV Premium 4K braucht drei Dinge: Sender, die tatsächlich in UHD ausgestrahlt werden, Server, die die höhere Datenrate auch abends liefern, und ein Gerät mit H.265-Decoder.</p>''',
    },
),

"iptv-geraete": dict(
    into={
        "welches-geraet": '''<p>Fast jeder IPTV Fernseher-Wunsch lässt sich erfüllen: Smart TVs laufen direkt mit einer App, ältere Geräte mit einem <a href="/iptv-stick/">IPTV Stick</a>. Details zu IPTV for Smart TV stehen unter <a href="/iptv-smart-tv/">IPTV Smart TV</a>.</p>''',
        "wlan": '''<p>Eine IPTV Box WiFi-Verbindung funktioniert also, wenn der Router nah steht und 5 GHz nutzt; für 4K und Fußball ist LAN die sichere Wahl.</p>''',
    },
),
}
