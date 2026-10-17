# Zweite Runde: mehr Tiefe für Geräte- und App-Seiten.
# "into" ergänzt einen bestehenden Abschnitt (per h2-id), "body" hängt nur wirklich neue Abschnitte an.
EXTEND = {

"iptv-smarters-pro": dict(
    app={"name": "IPTV Smarters Pro", "os": "Android, Fire OS, iOS, tvOS, Windows, macOS", "url": "https://www.iptvsmarters.com/"},
    into={
        "was-ist": '''<p>Im Netz finden Sie viele Schreibweisen: Smarters IPTV, Smarters IPTV Pro, Smarters Pro IPTV, IPTV Smarter Pro, IP Smarter Pro, IP TV Smarter Pro oder IP TV Smart Pro. Gemeint ist fast immer die offizielle App IPTV Smarters Pro; Smarters IPTV Lite ist die erwähnte Lite-Variante. Vorsicht bei Apps mit Namen wie „Smarters TV“ oder „Smarters TV Pro“ aus unbekannten Quellen: Das können Nachbauten sein. Die offizielle Seite des Entwicklers erreichen Sie unter iptvsmarters.com (oft als „IPTV Smarters com“ gesucht).</p>''',
        "fire-tv": '''<p>Ob in Anleitungen „IPTV Smarters on Firestick“, „IPTV Smarters Fire Stick“, „IPTV Smarters Firestick“ oder „Smarters Pro Firestick“ steht: Gemeint ist immer dieselbe Installation. Läuft IPTV Smarters Pro Fire TV Stick-seitig nach einem Update nicht mehr, helfen meist drei Schritte: App-Cache leeren, Stick neu starten, Zugangsdaten neu eintragen. Bei Ruckeln mit IPTV Smarters Pro Fire Stick oder IPTV Smarters Pro Firestick stellen Sie im Player den Hardware-Decoder ein.</p>''',
        "kundenservice": '''<p>Kurz gesagt: Der IPTV Smarters Customer Service des Entwicklers kümmert sich um die App, wir um Ihren Zugang.</p>''',
    },
    body='''
<h2 id="premium-abo">IPTV Smarters free, Premium und „Subscription“</h2>
<p>Die App selbst ist kostenlos (IPTV Smarters free). Je nach Plattform bietet der Entwickler zusätzlich eine werbefreie oder erweiterte Version an, die oft als IPTV Smarters Pro Premium oder IPTV Smarters Premium bezeichnet wird. Den IPTV Smarters Pro Price für solche Extras legt der Entwickler fest; für das Fernsehen sind sie nicht nötig.</p>
<p>Wird irgendwo eine „IPTV Smarters Pro Subscription“ oder „IPTV Smarters Subscription“ verkauft, ist das immer das Abo eines IPTV-Anbieters, nie ein Angebot des App-Entwicklers. Bei uns kostet das Abo ab 4,08 € im Monat im Jahrespaket, siehe <a href="/preise/">Preise</a>.</p>

<h2 id="live-tv">IPTV Smarters Pro Live TV, Filme und Catch-Up</h2>
<p>Im Bereich „Live TV“ von IPTV Smarters Pro Live finden Sie alle Sender nach Gruppen sortiert, mit Programmführer. „Movies“ und „Series“ öffnen die Filmbibliothek mit Cover und Beschreibung, „Catch Up“ zeigt verpasste Sendungen der letzten Tage, sofern der Sender das unterstützt. Über das Stern-Symbol legen Sie Favoriten an, die in allen Bereichen oben erscheinen.</p>
''',
),

"iptv-apps": dict(
    kw_remove=["extreme iptv", "upiptv", "pandar tv"],
    into={
        "vergleich": '''<p>Wer international nach „best IPTV player“, „best player IPTV“ oder auf Deutsch nach „bester IPTV Player“ sucht, findet meist die Apps aus dieser Tabelle. Unser Tipp: Testen Sie zwei Apps mit denselben Zugangsdaten und behalten Sie die, deren Bedienung Ihnen besser gefällt. Für jede App IPTV-Kombination gilt: Die Sender kommen aus dem Abo, nicht aus der App.</p>''',
        "weitere": '''<h3>Ähnliche Namen, die oft verwechselt werden</h3>
<ul>
  <li><strong>GSE IPTV:</strong> Kurzform für GSE Smart IPTV.</li>
  <li><strong>OTT Navigator Premium:</strong> die kostenpflichtige Stufe des OTT Navigator mit zusätzlichen Funktionen.</li>
  <li><strong>IPTVX Apple TV und IPTVX Android:</strong> IPTVX ist für Apple-Geräte gebaut; eine offizielle Android-Version ist uns nicht bekannt.</li>
  <li><strong>Duplecast IPTV:</strong> Player für Smart-TVs, die Playlist übertragen Sie über eine Webseite.</li>
  <li><strong>IPTV Pro (IPTVPro), IPTV Stream Player (IPTV Streamplayer), Simple IPTV (SimpleIPTV) und OTT IPTV (OTTIPTV):</strong> einfache Player, teils nur für einzelne Plattformen.</li>
  <li><strong>Smart IPTV Pro, IPTV Smart Pro, Smart Player TV und IP TV Smart Player:</strong> Namen verschiedener Apps, die leicht mit <a href="/smart-iptv/">Smart IPTV</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> verwechselt werden. Prüfen Sie im Store den Entwickler.</li>
</ul>
<h3>Plex IPTV und Jellyfin IPTV</h3>
<p>In Jellyfin fügen Sie die M3U-URL als Live-TV-Tuner und eine EPG-Quelle hinzu. Plex erwartet für Live-TV einen Tuner, deshalb nutzen manche ein Zusatzprogramm, das die M3U-Liste als Tuner ausgibt. Für die meisten Haushalte ist eine normale IPTV-App einfacher.</p>''',
    },
    body='''
<h2 id="browser">IPTV Browser und Web-Player</h2>
<p>Ein IPTV Browser oder Web-Player klingt praktisch, scheitert aber oft daran, dass Browser unverschlüsselte Streams auf verschlüsselten Seiten blockieren. Am PC ist <a href="/vlc-iptv/">VLC</a> zuverlässiger, Details stehen unter <a href="/iptv-pc-mac/">IPTV am PC und Mac</a>.</p>
''',
),

"iptv-smart-tv": dict(
    kw_remove=["iptv google tv", "iptv chromecast", "iptv smarters chromecast", "tivimate chromecast",
               "iptv roku", "iptv roku tv", "iptv on roku tv", "iptv smarters pro roku"],
    into={
        "system": '''<p>Für IPTV Smart TV und IP TV Smart TV gilt deshalb: erst das System prüfen, dann die App wählen. Bei IPTV Philips-, IPTV Hisense-, IPTV Panasonic- und IPTV Toshiba-Geräten hängt es vom Modell ab, welche Zeile der Tabelle passt.</p>''',
        "android-tv": '''<p>TiviMate Android TV ist für die Fernbedienung optimiert und unsere erste Empfehlung, IPTV Smarters Pro Android TV die einfachere kostenlose Alternative. Auch eine Smart IPTV Android TV-Version gibt es; sie wird über die Website des Entwicklers installiert, Details unter <a href="/smart-iptv/">Smart IPTV</a>. Für Smart IPTV Philips-Modelle ohne Android, etwa mit Titan OS, ist ein Stick die verlässlichste Lösung.</p>''',
        "vidaa": '''<p>Ob für IPTV Hisense VIDAA oder Smart IPTV Hisense VIDAA eine passende App im Store steht, ändert sich je nach Modelljahr. Prüfen Sie es direkt am Fernseher, bevor Sie etwas kaufen.</p>''',
    },
    swap={
        "chromecast": '''<h2 id="chromecast">Chromecast, Google TV und Roku</h2>
<p>Chromecast mit Google TV und der Google TV Streamer sind vollwertige Google-TV-Geräte, ältere Chromecasts können nur vom Handy übertragen, und auf Roku gibt es keine empfehlenswerten IPTV Apps für Xtream-Zugänge. Den ausführlichen Vergleich aller Sticks finden Sie unter <a href="/iptv-stick/">IPTV Stick</a>.</p>''',
        "roku": "",
    },
),

"iptv-pc-mac": dict(
    kw_add=["my iptv"],
    into={
        "optionen": '''<p>Für IPTV PC- und IPTV Laptop-Nutzung reicht eine dieser Lösungen. Unter Windows gibt es außerdem eigene IPTV Player Win-Programme wie den MyIPTV Player aus dem Microsoft Store (oft als „My IPTV“ gesucht), die wir nennen, aber nicht selbst betreuen.</p>''',
        "smarters": '''<p>Den IPTV Smarters Pro Windows Download finden Sie auf der offiziellen Seite im Bereich Downloads; IPTV Smarters Pro PC und Smarters Pro PC sind dieselbe App. Für den Mac heißt die Version IPTV Smarters Mac bzw. IPTV Smarters Pro Mac. Auf einem IPTV MacBook mit Apple-Chip laufen für IPTV Smarters Pro MacBook-Nutzer zusätzlich manche iPad-Apps aus dem App Store.</p>''',
        "browser": '''<p>Eine IPTV Web Browser-Lösung wie IPTV Smarters Web bzw. ein IPTV Smarters Online-Player wird von manchen Anbietern über ein eigenes Portal angeboten. Reine „M3U online“-Player scheitern oft daran, dass Browser unverschlüsselte (http-)Streams auf verschlüsselten Seiten blockieren.</p>''',
        "tivimate": '''<p>Eine offizielle Version „TiviMate for PC“, „TiviMate PC“ oder „TiviMate Mac“ gibt es nicht. Auch Smart IPTV Mac existiert nicht als Desktop-App, Smart IPTV ist für Fernseher gebaut.</p>''',
    },
),

"iptv-fire-tv-stick": dict(
    kw_remove=["ip tv stick", "iptv stick", "iptv tv stick", "iptv sticks"],
    into={
        "welcher-stick": '''<p>Für Fire TV IPTV eignen sich alle aktuellen Amazon-Geräte. Wer IPTV Amazon-seitig auf einem Fernseher mit eingebautem Fire TV nutzt, geht genauso vor; eine extra „IPTV Box Amazon“ brauchen Sie nicht. Für Amazon Fire Stick IPTV am 4K-Fernseher empfehlen wir den 4K Max, für den IPTV Amazon Stick im Zweitzimmer reicht das HD-Modell. Wie sich Fire TV gegen Google TV und Roku schlägt, zeigt <a href="/iptv-stick/">IPTV Stick im Vergleich</a>.</p>''',
        "anleitung": '''<p>In Anleitungen heißt dieser Weg oft „IPTV Downloader“, „IPTV Smarters Downloader“ oder „Smart IPTV Downloader“: Gemeint ist immer die App Downloader mit der offiziellen Adresse des App-Entwicklers. Für Kurzcodes wie „Firestick ly73pr“ gilt die Warnung aus Schritt 2.</p>''',
        "beste-app": '''<p>Wer nach „bester IPTV Player für Fire TV Stick kostenlos deutsch“ sucht, landet meist bei IPTV Smarters Pro. Alle vier Apps laufen als IPTV for Firestick-Lösung mit unseren Zugangsdaten; für IPTV Fire Stick-Einsteiger empfehlen wir Smarters, für Vielseher TiviMate. Eine Übersicht für alle Geräte finden Sie unter <a href="/iptv-apps/">IPTV Apps</a>.</p>''',
    },
    body='''
<h2 id="alltag">IPTV Firestick: Tipps für den Alltag</h2>
<ul class="check-list">
  <li><svg><use href="#i-check"/></svg>Stick nicht direkt hinter dem Fernseher verstecken, besser mit der mitgelieferten HDMI-Verlängerung</li>
  <li><svg><use href="#i-check"/></svg>Einmal pro Woche neu starten: Einstellungen → Mein Fire TV → Neustart</li>
  <li><svg><use href="#i-check"/></svg>Apps aus Downloader aktualisieren sich nicht über den Appstore, prüfen Sie Updates selbst</li>
  <li><svg><use href="#i-check"/></svg>Nicht benötigte Apps löschen, damit genug Speicher für EPG und Filme bleibt</li>
</ul>
''',
),

"tivimate": dict(
    app={"name": "TiviMate", "os": "Android TV, Fire OS, Google TV", "url": "https://tivimate.com/"},
    into={
        "installieren": '''<p>TiviMate Fire TV, TiviMate Fire TV Stick oder TiviMate Firestick: Die Installation läuft immer über Downloader, weil TiviMate nicht im Amazon Appstore steht. TiviMate on Firestick bzw. TiviMate for Firestick läuft am besten auf dem 4K oder 4K Max, ältere Sticks laden große Senderlisten langsamer. Firestick TiviMate auf dem Fire TV Cube funktioniert identisch. Laden Sie die App nur über die offizielle TiviMate Website tivimate.com oder den Google Play Store.</p>''',
        "einrichten": '''<p>TiviMate M3U-Playlists funktionieren, wir empfehlen aber den Xtream-Login, weil TiviMate dann Logos, EPG und Filmbibliothek automatisch lädt. Mit einem TiviMate IPTV-Zugang von IPTV Welt Premium erhalten Sie beides.</p>''',
        "premium": '''<p>Zu den häufigen Fragen nach TiviMate Kosten, TiviMate Price, TiviMate Premium Price oder TiviMate Premium Cost: Feste Beträge nennen wir bewusst nicht, weil der Entwickler sie gelegentlich ändert. Die TiviMate Premium Subscription bzw. TiviMate Subscription gibt es als Abo oder Einmalkauf, verknüpft mit einem TiviMate Account. Diese Lizenz betrifft nur den Player; Sender und Filme kommen aus Ihrem IPTV-Abo.</p>''',
    },
),

"m3u-playlist": dict(
    into={
        "m3u-m3u8": '''<p>Deshalb sind M3U IPTV, M3U8 IPTV und IPTV M3U8 in der Praxis austauschbar. Ob Sie die Datei IPTV M3U8 List, M3U8 List, M3U8 Liste oder M3U Lista nennen: Entscheidend ist, dass Ihre App die Adresse laden kann. Manche Anbieter verschicken Dateien mit Namen wie tv.m3u oder m.m3u IPTV-Listen; Apps lesen sie alle gleich.</p>''',
        "gratis": '''<p>Das gilt für jede angeblich kostenlose IPTV Play List und jede M3U IP TV-Sammlung aus Foren.</p>''',
        "pflege": '''<p>Eine gute IPTV M3U Playlist Deutsch bzw. IPTV Playlist Deutsch ist nach Gruppen sortiert (Deutschland, Sport, Filme, Kinder, International), hat Logos und eine EPG-Adresse. In unserer IPTV M3U Liste (IPTV M3U List) stehen die deutschen Sender ganz oben.</p>''',
    },
    body='''
<h2 id="m3u-test">IPTV M3U Test: Playlist in 2 Minuten prüfen</h2>
<p>Für einen schnellen IPTV M3U Test öffnen Sie die Adresse in <a href="/vlc-iptv/">VLC</a> über „Medien → Netzwerkstream öffnen“. Erscheint die Senderliste, ist die IPTV M3U-Liste in Ordnung. Läuft ein einzelner Sender nicht, liegt es am Stream, nicht an der Liste. Bei Fehlermeldungen hilft die <a href="/iptv-hilfe/">IPTV Hilfe</a>.</p>
''',
),

"iptv-samsung-tv": dict(
    into={
        "apps": '''<p>Samsung-Fernseher laufen mit Tizen, deshalb brauchen IPTV Samsung TV-Geräte eine App aus dem Samsung App Store. Für IPTV Samsung Tizen bzw. IPTV Tizen allgemein ist der IBO Player die verlässlichste Wahl. Taucht IPTV Smarters Samsung bzw. IPTV Smarters Samsung TV oder IPTV Smarters Pro Samsung TV bei Ihrem Modell noch im Store auf, können Sie es nutzen; sonst ist der IBO Player der Ersatz. TiviMate Samsung TV-Versionen und XCIPTV Samsung-Apps gibt es nicht.</p>''',
        "smart-iptv": '''<p>Ob SIPTV Samsung-Modelle aktuell im Store unterstützt, hängt vom Modell ab. Auf einem älteren Smart IPTV Samsung Fernseher läuft die App oft weiter, Smart IPTV Tizen-Neuinstallationen sind aber nicht immer möglich.</p>''',
        "modelle": '''<p>So ist IPTV for Samsung TV mit jedem Baujahr möglich, notfalls über einen <a href="/iptv-stick/">IPTV Stick</a>. Auf IPTV Samsung Smart TV-Modellen ab 2017 brauchen Sie in der Regel kein Zusatzgerät, IPTV Samsung funktioniert dort direkt mit der App.</p>''',
    },
),

"iptv-box": dict(
    into={
        "vergleich": '''<p>Zur TVIP S-Box v605 (auch TVIP S-Box 605 oder kurz TVIP 605): Sie startet wahlweise mit Linux oder Android und nutzt im Linux-Modus ein Portal ähnlich wie eine MAG Box. Die IPTV Nvidia Shield gilt seit Jahren als eine der schnellsten Boxen; mit TiviMate und aktivierter Bildwiederholraten-Anpassung läuft Fußball in 50 Hz ohne Ruckler.</p>''',
        "kaufkriterien": '''<p>Ob Sie es IPTV Box Android, IPTV TV Box Android, Box Android IPTV oder Box IPTV Android nennen: Entscheidend sind die Punkte oben. Eine IPTV Set Top Box bzw. Set Top Box IPTV-Lösung hat gegenüber einem Stick meist mehr Leistung, einen LAN-Anschluss und bessere Kühlung; für den Zweitfernseher reicht ein <a href="/iptv-stick/">IPTV Stick</a>. Bei Alibaba IPTV- und IPTV AliExpress-Angeboten kommen zu den Software-Risiken Zoll und Einfuhrumsatzsteuer hinzu.</p>''',
        "preise": '''<p>Bevor Sie über den IPTV Box Price nachdenken, machen Sie einen IPTV Box Test auf einem vorhandenen Gerät, etwa dem Handy oder Smart TV, mit unserem <a href="/kostenloser-test/">kostenlosen 24-Stunden-Zugang</a>. Läuft das Programm dort, brauchen Sie nur noch die Box.</p>''',
        "sky": '''<p>Eine IPTV Box Sky im engeren Sinn gibt es also nur von Sky selbst.</p>''',
    },
),

"smart-iptv": dict(
    app={"name": "Smart IPTV (SIPTV)", "os": "Tizen, webOS, Android TV, Fire OS"},
    into={
        "was-ist": '''<p>Im Netz begegnen Ihnen auch Namen wie „App Smart IPTV“, „IP Smart IPTV“ oder Adressen mit „smart iptv com“ und „IPTV Smart net“. Nicht jede davon gehört zum Entwickler; nutzen Sie die Adresse, die die App selbst anzeigt.</p>''',
        "geraete": '''<p>Smart IPTV Fire Stick bzw. Smart IPTV Firestick ist möglich, aber nicht die beste Wahl: <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a> laden die Playlist direkt, ohne MAC-Upload. Für Smart IPTV herunterladen gilt: nur aus dem Store des Fernsehers oder von der offiziellen Website.</p>''',
        "einrichten": '''<p>Die Seite heißt Smart IPTV My List bzw. SIPTV My List; die hochgeladene Smart IPTV List (SIPTV List) erscheint nach dem Neustart.</p>''',
        "kosten": '''<p>Eine „Smart IPTV Premium“-Version mit Sendern gibt es nicht: Smart IPTV Kosten fallen nur für die App an. Für den Smart IPTV Test der Sender nutzen Sie unseren <a href="/kostenloser-test/">kostenlosen 24-Stunden-Test</a>.</p>''',
    },
),

"mag-box": dict(
    into={
        "modelle": '''<p>Kurz eingeordnet: Infomir MAG 254 und MAG 256 sind die ältere Full-HD-Generation, die MAG Box 322 (Infomir MAG 322) ist die solide Wahl mit H.265, die MAG 420 bringt 4K. Wer neue MAG IPTV Boxes kauft, sollte auf H.265 achten. Jede MAG TV Box verbindet sich mit einem Portal und zeigt die Sender ohne zusätzliche App, das macht MAG IPTV so einfach.</p>''',
        "stb-emu": '''<p>Für STBEmu IPTV brauchen Sie die Portal-Adresse und eine MAC, die wir für Sie freischalten.</p>''',
    },
),

"iptv-android": dict(
    into={
        "apps": '''<p>Für IPTV Android-Handys und Tablets ist diese Auswahl an Application IPTV Android-Apps bewährt. Der beste IPTV Player Android-seitig für Einsteiger ist IPTV Smarters Pro Android (auch IPTV Smarters Android genannt), für Fortgeschrittene OTT Navigator. Smart IPTV Android und SSIPTV Android gibt es ebenfalls, sie sind aber für Fernseher gebaut. Wer nach „beste IPTV Player Android“ oder „IPTV Player Android“ sucht, findet weitere Optionen unter <a href="/iptv-apps/">IPTV Apps</a>.</p>''',
        "einrichten": '''<p>Achten Sie bei IPTV Smarters Pro Google Play-Downloads auf den richtigen Entwickler, es gibt Apps mit ähnlichem Namen.</p>''',
    },
),

"iptv-lg-tv": dict(
    into={
        "apps": '''<p>Für IPTV LG TV, IPTV LG Smart TV und IPTV LG webOS ist der IBO Player unsere Empfehlung, Smart IPTV LG ist ebenfalls weit verbreitet. Für IPTV for LG webOS-Modelle ab etwa 2016 klappt die Installation meist problemlos, siehe die webOS-Versionen weiter unten.</p>''',
        "smarters": '''<p>Das gilt auch für IPTV Smarters Pro LG und XCIPTV LG TV: Wer genau diese Apps möchte, nutzt sie auf einem Stick am LG-Fernseher, sonst läuft IPTV LG Smart mit dem IBO Player.</p>''',
    },
),

"iptv-apple-tv-iphone": dict(
    into={
        "apple-tv": '''<p>IPTV Smarters Apple TV bzw. IPTV Smarters Pro Apple TV finden Sie im tvOS App Store, je nach Version auch als Smarters Player Lite.</p>''',
        "iphone": '''<p>Für IPTV iPhone und IPTV iPad sind IPTV Smarters Pro iPhone (bzw. Smarters Player Lite), IPTVX und GSE Smart IPTV die bekanntesten Apps.</p>''',
        "tivimate": '''<p>Für TiviMate Apple TV-Wünsche gilt deshalb: Es gibt keine Version für tvOS. Die TiviMate Companion iPhone-App ersetzt den Player nicht, sie verwaltet nur das Premium-Konto.</p>''',
    },
),

"iptv-receiver": dict(
    into={
        "arten": '''<p>IPTV for Receiver heißt also nicht zwingend ein neues Gerät: Viele vorhandene Sat-Receiver können IPTV zusätzlich abspielen.</p>''',
        "enigma2": '''<p>Für Gigablue IPTV gehen Sie genauso vor wie bei anderen Enigma2-Geräten; achten Sie auf ein aktuelles Image, damit H.265-Streams laufen. Mit IPTV Enigma2 erscheinen die Sender danach wie gewohnte Kanäle.</p>''',
        "dreamlink": '''<p>Beim Dreamlink T3 tragen Sie die Xtream-Daten direkt in der vorinstallierten Oberfläche oder in einer App ein.</p>''',
        "aufnahme": '''<p>Bevor Sie für IPTV DVR ein neues Gerät kaufen, machen Sie einen IPTV Receiver Test mit unserem <a href="/kostenloser-test/">kostenlosen 24-Stunden-Zugang</a> auf einem vorhandenen Gerät.</p>''',
    },
),

"formuler": dict(
    into={
        "modelle": '''<p>Wer eine gebrauchte Formuler TV Box kauft, findet oft noch Formuler Z7 oder Formuler Z7+. Für Neukäufe sind die Z10- und Z11-Reihen die bessere Wahl, die Formuler Z8 Pro liegt in der Mitte und die Formuler Z Neo ist der günstige Einstieg.</p>''',
    },
),

"xciptv": dict(
    app={"name": "XCIPTV", "os": "Android, Fire OS, Android TV"},
    into={
        "was-ist": '''<p>XCIPTV Free ist die normale Version des Players. Manche Anbieter verteilen angepasste Versionen mit eigenem Logo; laden Sie die App trotzdem nur aus einer Quelle, der Sie vertrauen.</p>''',
        "installieren": '''<p>Für XCIPTV Fire TV, XCIPTV Fire TV Stick und XCIPTV Firestick ist der Ablauf identisch. Auf älteren Sticks läuft XCIPTV oft flüssiger als größere Apps.</p>''',
    },
),

"ss-iptv": dict(
    app={"name": "SS IPTV", "os": "webOS, Tizen, Android"},
    into={
        "einrichten": '''<p>Die offizielle Seite ist ss-iptv.com; Kopien mit ähnlicher Adresse, etwa „ssiptv com“, sollten Sie meiden. Ihre SSIPTV List erscheint danach als Kachel, und SSIPTV M3U-Links aktualisieren sich automatisch, wenn Sie sie als externe Playlist hinterlegen.</p>''',
    },
),

"kodi-iptv": dict(
    app={"name": "Kodi", "os": "Windows, macOS, Linux, Android, Fire OS", "url": "https://kodi.tv/"},
    into={
        "was-ist": '''<p>Kodi hieß früher XBMC. Anleitungen zu Kodi XBMC IPTV gelten deshalb im Grundsatz weiter, die Menüs heißen heute nur anders.</p>''',
        "einrichten": '''<p>Nach dem Neustart steht Kodi Live TV mit allen Sendern im Menüpunkt „TV“.</p>''',
        "tipps": '''<p>Bei Kodinerds IPTV-Fragen lohnt der Blick in die Forenbereiche zum PVR IPTV Simple Client. Inoffizielle Addons, die „gratis Fernsehen“ versprechen, sind dagegen oft unzuverlässig.</p>''',
    },
),

"vlc-iptv": dict(
    app={"name": "VLC media player", "os": "Windows, macOS, Linux, Android, iOS", "url": "https://www.videolan.org/vlc/"},
    into={
        "pc": '''<p>Ob Sie es IPTV VLC, VLC IP TV oder IP TV VLC nennen: Mehr Schritte sind für den Anfang nicht nötig.</p>''',
    },
),

"ibo-player": dict(
    app={"name": "IBO Player Pro", "os": "Tizen, webOS, Android, Fire OS, iOS, tvOS"},
    into={
        "warum": '''<p>Unter IPTV IBO verstehen die meisten den IBO Player oder den IBO Player Pro. Beide sind reine Player ohne eigene Sender.</p>''',
    },
),

"smart-one-iptv": dict(
    app={"name": "Smart One IPTV", "os": "Tizen, webOS, Android"},
    into={
        "tipps": '''<p>Viele suchen nach „Smarte One IPTV“; gemeint ist die App Smart One IPTV. Prüfen Sie im Store den Entwickler.</p>''',
    },
    body='''
<h2 id="vergleich-ibo">Smart One IPTV oder IBO Player?</h2>
<p>Beide Apps funktionieren nach demselben Prinzip: App öffnen, MAC-Adresse notieren, Playlist auf der Website hinterlegen. Der IBO Player Pro zeigt Filme und Serien mit Covern übersichtlicher an und ist im 12-Monats-Paket als Premium-Version enthalten. Smart One IPTV ist eine gute Wahl, wenn der IBO Player auf Ihrem Modell nicht verfügbar ist oder Sie eine schlichtere Oberfläche bevorzugen.</p>

<h2 id="fehler">Häufige Fehler</h2>
<ul>
  <li><strong>Playlist erscheint nicht:</strong> App komplett schließen und neu öffnen, MAC-Adresse auf Tippfehler prüfen (0 und O, B und 8).</li>
  <li><strong>Kein Programmführer:</strong> In den App-Einstellungen das EPG aktualisieren.</li>
  <li><strong>Testphase abgelaufen:</strong> Die App beim Entwickler aktivieren; die Sender selbst kommen aus Ihrem IPTV-Abo.</li>
</ul>
''',
),

"flix-iptv": dict(
    app={"name": "Flix IPTV", "os": "Tizen, webOS, Android, Fire OS"},
    body='''
<h2 id="fehler">Flix IPTV: häufige Fehler</h2>
<ul>
  <li><strong>Playlist nicht gefunden:</strong> MAC-Adresse auf der Upload-Seite exakt so eingeben, wie die App sie anzeigt.</li>
  <li><strong>Filme laden langsam:</strong> Beim ersten Start wird die Filmbibliothek komplett geladen; per LAN geht das schneller.</li>
  <li><strong>App nach Update leer:</strong> Playlist auf der Website erneut speichern und App neu starten.</li>
</ul>
<p>Für Live-TV mit großem Programmraster sind <a href="/tivimate/">TiviMate</a> auf Android TV oder der <a href="/ibo-player/">IBO Player</a> auf Samsung und LG oft übersichtlicher. Da alle Apps dieselben Zugangsdaten nutzen, können Sie jederzeit wechseln.</p>
''',
),

"set-iptv": dict(
    app={"name": "SET IPTV", "os": "Tizen, webOS, Android"},
),
}
