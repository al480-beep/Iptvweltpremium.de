# Zweite Runde: Seiten für Keyword-Cluster, die vorher nur als Nebenthema liefen
PAGES = [
dict(
    slug="iptv-stream", parent="ratgeber", nav="IPTV Stream", priority="0.8",
    card="Live-TV als Stream über das Internet: wie es funktioniert und was Sie brauchen.",
    kw=["iptv stream", "ip tv streaming", "stream iptv", "iptv live", "iptv tv", "iptv ip"],
    title="IPTV Stream: Live-TV über das Internet streamen (2026)",
    desc="IPTV Stream einfach erklärt: Live-TV über die Internetleitung streamen, welche Bandbreite Sie brauchen und wie Sie Ruckeln vermeiden. Jetzt gratis testen.",
    eyebrow="Live-Streaming", h1='IPTV Stream: <span class="grad-text">Fernsehen live aus dem Internet</span>',
    lead="Kein Kabelanschluss, keine Satellitenschüssel: Beim IPTV Streaming kommt das Fernsehprogramm über Ihre Internetleitung. So funktioniert es und so läuft es flüssig.",
    answer="Ein IPTV Stream ist ein Fernsehsender, der über das Internetprotokoll (IP) übertragen wird statt über Kabel, Satellit oder Antenne. Sie brauchen eine Internetleitung mit mindestens 16 Mbit/s für HD oder 30 Mbit/s für 4K, ein Gerät mit IPTV-App und Zugangsdaten. Dann läuft IPTV TV live wie klassisches Fernsehen, mit Programmführer und Umschalten per Fernbedienung.",
    body='''
<h2 id="was">Was ist ein IPTV Stream?</h2>
<p>IPTV steht für Internet Protocol Television. Bei IPTV TV wird jeder Sender als Datenstrom über das IP-Netz geschickt, genau wie ein Video bei YouTube oder Netflix. Der Unterschied: Ein Live-Sender läuft fortlaufend, und Sie schalten zwischen den Kanälen um wie beim normalen Fernsehen. Deshalb sprechen manche auch von „IPTV IP“, gemeint ist immer dasselbe: Fernsehen über das Internetprotokoll.</p>
<p>Ob Sie IPTV live auf dem Fernseher, auf dem Handy oder am PC schauen, ist nur eine Frage der App. Die Zugangsdaten bleiben gleich. Mehr zu den Grundlagen lesen Sie unter <a href="/was-ist-iptv/">Was ist IPTV?</a></p>

<h2 id="ablauf">So kommt der Stream auf Ihren Bildschirm</h2>
<ol class="howto">
  <li><b>Der Sender wird eingespeist</b> und in ein Streaming-Format wie HLS oder MPEG-TS umgewandelt.</li>
  <li><b>Server verteilen den Stream</b> an alle Zuschauer, die diesen Kanal gerade sehen.</li>
  <li><b>Ihre App lädt die Senderliste</b> über eine M3U-Playlist oder den Xtream-Login und zeigt den Programmführer.</li>
  <li><b>Sie schalten um</b> und der Player puffert ein paar Sekunden, bevor das Bild startet.</li>
</ol>

<h2 id="bandbreite">Welche Internetleitung brauchen Sie zum Streamen?</h2>
<div class="matrix"><div class="matrix-scroll"><table>
  <thead><tr><th scope="col">Qualität</th><th scope="col">Empfohlene Leitung pro Gerät</th><th scope="col">Typische Nutzung</th></tr></thead>
  <tbody>
    <tr><td>SD</td><td>ab 8 Mbit/s</td><td>Handy unterwegs, schwache Leitungen</td></tr>
    <tr><td>HD / Full HD</td><td>16 Mbit/s</td><td>Die meisten Sender, Fußball, Nachrichten</td></tr>
    <tr><td>4K / UHD</td><td>30 Mbit/s</td><td>Große Fernseher, ausgewählte Sender und Filme</td></tr>
  </tbody>
</table></div></div>
<p>Schauen mehrere Personen gleichzeitig, addieren sich die Werte. Wichtiger als die reine Geschwindigkeit ist eine stabile Verbindung: Ein Fernseher am LAN-Kabel oder im 5-GHz-WLAN streamt deutlich ruhiger als ein Stick hinter zwei Wänden. Tipps dazu stehen in unserer <a href="/iptv-hilfe/">IPTV Hilfe</a>.</p>

<h2 id="vergleich">IPTV Stream oder klassisches Fernsehen?</h2>
<div class="pros-cons">
  <div><h3>Vorteile</h3><ul>
    <li>Keine Schüssel, kein Kabelanschluss, kein Receiver nötig</li>
    <li>Sender aus vielen Ländern in einer App</li>
    <li>Catch-Up und Filmbibliothek auf Abruf</li>
    <li>Läuft auf Fernseher, Stick, Handy und PC</li>
  </ul></div>
  <div><h3>Nachteile</h3><ul>
    <li>Abhängig von einer stabilen Internetleitung</li>
    <li>Einige Sekunden Verzögerung gegenüber Satellit</li>
    <li>Qualität hängt stark vom Anbieter ab</li>
  </ul></div>
</div>

<h2 id="geraete">Auf welchen Geräten läuft IPTV live?</h2>
<p>Am beliebtesten ist der <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, gefolgt von <a href="/iptv-samsung-tv/">Samsung</a> und <a href="/iptv-lg-tv/">LG Smart TVs</a>. Auch eine <a href="/iptv-box/">Android TV Box</a>, ein <a href="/iptv-apple-tv-iphone/">iPhone oder Apple TV</a> und der <a href="/iptv-pc-mac/">PC</a> eignen sich. Die passenden Apps finden Sie in der Übersicht <a href="/iptv-apps/">IPTV Apps</a>.</p>

<h2 id="starten">Den ersten Stream in 10 Minuten starten</h2>
<p>Um Stream IPTV-Kanäle selbst auszuprobieren, fordern Sie den <a href="/kostenloser-test/">kostenlosen 24-Stunden-Test</a> an, installieren Sie eine App wie <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> und tragen Sie die Zugangsdaten aus der E-Mail ein. Danach sehen Sie die Senderliste mit allen deutschen Programmen. Wie das Schritt für Schritt geht, zeigt die Anleitung <a href="/iptv-einrichten/">IPTV einrichten</a>.</p>
''',
    faq=[
        ("Ist ein IPTV Stream dasselbe wie Streaming bei Netflix?", "Technisch ähnlich, beides läuft über das Internet. Bei IPTV schauen Sie aber vor allem lineare Live-Sender mit Programmführer, bei Netflix nur Inhalte auf Abruf."),
        ("Warum ist der IPTV Stream ein paar Sekunden später als Satellit?", "Der Stream wird umgewandelt, verteilt und von Ihrer App gepuffert. Das kostet meist einige Sekunden. Bei Fußball hören Sie den Torjubel der Nachbarn deshalb manchmal zuerst."),
        ("Brauche ich für IPTV TV einen bestimmten Internetanbieter?", "Nein. Unser IPTV läuft über jede Internetleitung, egal ob Telekom, Vodafone, 1&amp;1, O2 oder Glasfaser vom Stadtwerk. Wichtig sind 16 Mbit/s für HD und eine stabile Verbindung."),
        ("Kann ich IPTV live unterwegs schauen?", "Ja, mit einer IPTV-App auf dem Handy oder Tablet. Im Mobilfunknetz verbraucht eine Stunde HD aber mehrere Gigabyte Datenvolumen."),
    ],
    related=["was-ist-iptv", "iptv-deutschland", "iptv-hilfe", "iptv-einrichten", "iptv-geraete", "kostenloser-test"],
),
dict(
    slug="iptv-stick", parent="iptv-geraete", nav="IPTV Stick", priority="0.8",
    card="Fire TV Stick, Google TV, Chromecast oder Roku: welcher Stick für IPTV taugt.",
    kw=["ip tv stick", "iptv stick", "iptv tv stick", "iptv sticks", "iptv google tv", "iptv chromecast",
        "iptv smarters chromecast", "tivimate chromecast", "iptv roku", "iptv roku tv", "iptv on roku tv", "iptv smarters pro roku"],
    title="IPTV Stick: Fire TV, Google TV, Chromecast & Roku im Vergleich",
    desc="Welcher IPTV Stick ist der richtige? Fire TV Stick, Google TV Streamer, Chromecast und Roku im Vergleich, mit passenden Apps und Tipps. Jetzt gratis testen.",
    eyebrow="Streaming-Sticks", h1='IPTV Stick: <span class="grad-text">welcher Stick passt zu Ihnen?</span>',
    lead="Ein Stick in den HDMI-Anschluss, App installieren, fertig: So wird aus fast jedem Fernseher ein IPTV-Gerät. Hier sehen Sie, welche Sticks sich eignen und welche nicht.",
    answer="Der beste IPTV Stick für die meisten Haushalte ist ein Fire TV Stick 4K oder ein Gerät mit Google TV, weil dort Apps wie IPTV Smarters Pro und TiviMate laufen. Ein klassischer Chromecast ohne Fernbedienung kann IPTV nur vom Handy übertragen. Auf Roku gibt es nur wenige IPTV-Apps, deshalb empfehlen wir Roku nicht als ersten IPTV Stick.",
    body='''
<h2 id="vergleich">IPTV Sticks im Vergleich</h2>
<p>Ein IPTV TV Stick ist ein Streaming-Stick, auf dem Sie eine IPTV-App installieren. Der Stick selbst enthält keine Sender, die kommen aus Ihrem Abo.</p>
<div class="matrix"><div class="matrix-scroll"><table>
  <thead><tr><th scope="col">Stick</th><th scope="col">System</th><th scope="col">IPTV-Apps</th><th scope="col">Eignung</th></tr></thead>
  <tbody>
    <tr><td>Fire TV Stick 4K / 4K Max</td><td>Fire OS</td><td>IPTV Smarters Pro, TiviMate, IBO Player, XCIPTV</td><td>Sehr gut</td></tr>
    <tr><td>Google TV Streamer, Chromecast mit Google TV</td><td>Google TV (Android TV)</td><td>TiviMate, IPTV Smarters Pro, OTT Navigator</td><td>Sehr gut</td></tr>
    <tr><td>Xiaomi TV Stick 4K und andere Android-TV-Sticks</td><td>Android TV</td><td>Wie Google TV, Apps aus dem Play Store</td><td>Gut</td></tr>
    <tr><td>Chromecast ohne Google TV (ältere Modelle)</td><td>Cast-Empfänger</td><td>Nur Übertragung vom Handy</td><td>Eingeschränkt</td></tr>
    <tr><td>Roku Streaming Stick</td><td>Roku OS</td><td>Wenige, meist einfache M3U-Player</td><td>Eingeschränkt</td></tr>
  </tbody>
</table></div></div>
<p>Die Angaben beziehen sich auf den Stand Oktober 2026. App-Angebote ändern sich, prüfen Sie deshalb vor dem Kauf den App Store des jeweiligen Geräts.</p>

<h2 id="fire-tv">Fire TV Stick: der Standard für IPTV</h2>
<p>Der Fire TV Stick ist in Deutschland der beliebteste IPTV Stick. Er ist günstig, hat eine Fernbedienung mit Sprachsteuerung und lädt fast jede IPTV-App, entweder aus dem Amazon Appstore oder über die App Downloader. Für 4K-Fernseher nehmen Sie das 4K-Modell, für ruckelfreies Umschalten am besten den 4K Max. Die vollständige Anleitung finden Sie unter <a href="/iptv-fire-tv-stick/">IPTV auf dem Fire TV Stick</a>.</p>

<h2 id="google-tv">IPTV mit Google TV und Chromecast</h2>
<p>Für IPTV Google TV-Geräte gilt: Geräte mit Google TV, etwa der Google TV Streamer oder der Chromecast mit Google TV, laufen mit Android TV. Dort installieren Sie IPTV-Apps direkt aus dem Google Play Store. TiviMate gilt auf Google TV als besonders komfortabel, weil es für die Fernbedienung gebaut ist. Google hat den Chromecast inzwischen durch den Google TV Streamer ersetzt, vorhandene Geräte funktionieren aber weiter.</p>
<h3>IPTV Chromecast ohne Google TV: Streams vom Handy übertragen</h3>
<p>Ältere Chromecast-Modelle ohne Fernbedienung können keine Apps installieren. Sie können aber einen Stream vom Smartphone auf den Fernseher „casten“. Die IPTV Smarters Chromecast-Funktion steckt in der Handy-App. Eine TiviMate Chromecast-Übertragung gibt es dagegen nicht, weil TiviMate eine reine TV-App ist. Für den Alltag ist ein Stick mit eigener Fernbedienung deutlich bequemer.</p>

<h2 id="roku">IPTV Roku: Stick und Roku TV</h2>
<p>Roku-Sticks und Fernseher mit Roku TV sind in Deutschland seltener. Für IPTV Roku gilt: Im Roku-Kanalstore gibt es nach unserem Kenntnisstand keine offizielle Version „IPTV Smarters Pro Roku“ und auch kein TiviMate. Einige einfache M3U-Player sind verfügbar, ihr Funktionsumfang wechselt aber häufig. Wer IPTV on Roku TV schauen möchte, also IPTV Roku TV ohne Umwege, steckt am einfachsten einen Fire TV Stick oder einen Google TV Streamer an einen freien HDMI-Anschluss.</p>

<h2 id="kauftipps">Worauf Sie beim Kauf eines IPTV Sticks achten sollten</h2>
<ul class="check-list">
  <li><svg><use href="#i-check"/></svg>Offizieller Stick von Amazon, Google oder Xiaomi statt „vorinstallierter IPTV Stick“ vom Marktplatz</li>
  <li><svg><use href="#i-check"/></svg>Mindestens 2 GB Arbeitsspeicher für flüssiges Umschalten</li>
  <li><svg><use href="#i-check"/></svg>5-GHz-WLAN oder ein Ethernet-Adapter für stabile Streams</li>
  <li><svg><use href="#i-check"/></svg>4K-Modell nur, wenn auch der Fernseher 4K kann</li>
</ul>
<p>Vorsicht bei Sticks, die mit „lebenslang gratis Fernsehen“ beworben werden: Dahinter stecken meist unbekannte Apps ohne Support. Ein normaler Stick plus ein seriöses Abo ist sicherer und auf Dauer günstiger. Einen Überblick über alle Geräte finden Sie unter <a href="/iptv-geraete/">IPTV Geräte</a>.</p>
''',
    faq=[
        ("Welcher IPTV Stick ist der beste?", "Für die meisten ist der Fire TV Stick 4K oder 4K Max die beste Wahl. Wer lieber Google-Dienste nutzt, nimmt einen Google TV Streamer. Beide laufen mit allen gängigen IPTV-Apps."),
        ("Funktioniert IPTV auf dem Chromecast?", "Mit Google TV ja, dort installieren Sie die App direkt. Ältere Chromecasts ohne Fernbedienung zeigen nur Streams, die Sie vom Handy übertragen, zum Beispiel aus IPTV Smarters."),
        ("Gibt es IPTV Smarters Pro für Roku?", "Nach unserem Kenntnisstand nicht als offizielle App. Auf Roku gibt es nur wenige einfache M3U-Player. Ein Fire TV Stick am selben Fernseher ist die zuverlässigere Lösung."),
        ("Brauche ich einen speziellen IPTV Stick?", "Nein. Ein normaler Streaming-Stick genügt, die IPTV-App installieren Sie selbst. Von vorkonfigurierten Sticks unbekannter Herkunft raten wir ab."),
    ],
    related=["iptv-fire-tv-stick", "iptv-box", "iptv-smart-tv", "tivimate", "iptv-smarters-pro", "iptv-geraete"],
),
dict(
    slug="iptv-georgien", parent="iptv-international", nav="IPTV Georgien", priority="0.6",
    card="Georgische Sender wie Imedi, Rustavi 2 und 1TV live in Deutschland schauen.",
    kw=["iptv ge", "iptv ge imedi", "imedi tv live iptv ge", "iptv ge live", "iptv ge rustavi2"],
    title="IPTV Georgien: Imedi, Rustavi 2 & 1TV live in Deutschland",
    desc="Georgisches Fernsehen in Deutschland: Imedi, Rustavi 2, 1TV und weitere Sender live per IPTV, zusammen mit allen deutschen Sendern. Jetzt 24h gratis testen.",
    eyebrow="Georgien", h1='IPTV Georgien: <span class="grad-text">georgische Sender live</span>',
    lead="Nachrichten aus Tiflis, Serien und Shows aus der Heimat: So schauen georgische Familien in Deutschland ihre Sender live, ohne Satellitenschüssel.",
    answer="Mit IPTV Welt Premium schauen Sie georgische Sender, soweit verfügbar, in der internationalen Gruppe der Playlist, zusammen mit allen deutschen Programmen. Häufig gesucht werden Imedi, Rustavi 2, der öffentlich-rechtliche Sender 1TV, Formula und Mtavari. Welche Sender aktuell laufen, sehen Sie im kostenlosen 24-Stunden-Test.",
    body='''
<h2 id="sender">Georgische Sender, nach denen häufig gesucht wird</h2>
<div class="matrix"><div class="matrix-scroll"><table>
  <thead><tr><th scope="col">Sender</th><th scope="col">Schwerpunkt</th></tr></thead>
  <tbody>
    <tr><td>1TV (Georgian Public Broadcaster)</td><td>Öffentlich-rechtlich: Nachrichten, Kultur, Sport</td></tr>
    <tr><td>Imedi TV</td><td>Nachrichten, Shows und Serien</td></tr>
    <tr><td>Rustavi 2</td><td>Nachrichten, Unterhaltung, Serien</td></tr>
    <tr><td>Formula TV</td><td>Nachrichten und Talk</td></tr>
    <tr><td>Mtavari</td><td>Nachrichten und Politik</td></tr>
  </tbody>
</table></div></div>
<p>Die Tabelle zeigt, wonach unsere Kunden fragen. Sie ist keine Garantie, dass jeder Sender jederzeit verfügbar ist. Die aktuelle Liste sehen Sie im <a href="/kostenloser-test/">kostenlosen Test</a>.</p>

<h2 id="iptv-ge">„IPTV GE“: was hinter der Suche steckt</h2>
<p>Viele Zuschauer suchen nach „IPTV GE“, „IPTV GE live“, „IPTV GE Imedi“, „Imedi TV live IPTV GE“ oder „IPTV GE Rustavi2“. Gemeint ist meist georgisches IPTV, also georgische Sender über das Internet. In Georgien selbst gibt es eigene IPTV-Dienste mit .ge-Adressen, die auf Kunden im Land ausgerichtet sind. IPTV Welt Premium ist ein davon unabhängiger Anbieter für Zuschauer in Deutschland, der georgische Programme neben deutschen Sendern anbietet.</p>
<p>Imedi TV live und andere Sender bieten teils selbst Livestreams auf ihren Websites an. Diese laufen allerdings nur im Browser und ohne Programmführer. Mit IPTV haben Sie alle Sender in einer App auf dem Fernseher.</p>

<h2 id="einrichten">So schauen Sie georgisches IPTV live auf dem Fernseher</h2>
<ol class="howto">
  <li><b>Test anfordern</b> und Zugangsdaten per E-Mail erhalten.</li>
  <li><b>App installieren</b>, zum Beispiel <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> auf dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder <a href="/ibo-player/">IBO Player</a> auf dem Smart TV.</li>
  <li><b>Gruppe „Georgia“ oder „International“ öffnen</b> und die georgischen Sender zu den Favoriten hinzufügen.</li>
</ol>

<h2 id="familie">Georgisch und Deutsch in einem Abo</h2>
<p>Ein Zugang reicht für die ganze Familie: Die Eltern schauen Imedi oder Rustavi 2, die Kinder das deutsche Programm. Mit einem Paket für 2 bis 5 Geräte läuft beides gleichzeitig. Alle Pakete sehen Sie auf der <a href="/preise/">Preisseite</a>, weitere Länder unter <a href="/iptv-international/">IPTV International</a>.</p>
''',
    faq=[
        ("Kann ich Imedi TV live in Deutschland schauen?", "Ja, über IPTV in der internationalen Gruppe, soweit der Sender verfügbar ist. Ob er aktuell läuft, sehen Sie im kostenlosen 24-Stunden-Test."),
        ("Ist IPTV Welt Premium dasselbe wie iptv.ge?", "Nein. Georgische IPTV-Dienste mit .ge-Adresse sind eigenständige Anbieter in Georgien. Wir sind ein unabhängiger Anbieter für Zuschauer in Deutschland."),
        ("Gibt es georgische Sender mit Programmführer?", "Für viele Sender gibt es einen Programmführer (EPG). Er erscheint automatisch in Apps wie TiviMate oder IPTV Smarters Pro."),
    ],
    related=["iptv-international", "iptv-russisch", "iptv-ex-yu", "kostenloser-test", "iptv-fire-tv-stick", "preise"],
),
]
