# Audit-Runde 3 (Teil 2): zweite Vertiefung für die kürzesten Seiten
EXTEND = {

"ratgeber": dict(
    body='''
<h2 id="glossar">Kleines IPTV-Glossar</h2>
<dl>
  <dt>EPG</dt><dd>Der elektronische Programmführer zeigt, was gerade und als Nächstes läuft. Er wird getrennt von den Sendern geladen.</dd>
  <dt>VOD</dt><dd>Video on Demand: Filme und Serien zum Abruf, unabhängig vom Live-Programm. Mehr dazu unter <a href="/iptv-filme-serien/">IPTV Filme &amp; Serien</a>.</dd>
  <dt>Xtream Codes</dt><dd>Eine Anmeldung mit Server, Benutzername und Passwort. Erklärt auf der Seite <a href="/xtream-codes/">Xtream Codes</a>.</dd>
  <dt>M3U</dt><dd>Eine Textdatei mit Sendern und Stream-Adressen. Details: <a href="/m3u-playlist/">M3U Playlist</a>.</dd>
  <dt>MAC-Adresse</dt><dd>Die Kennung Ihres Geräts im Netzwerk. Manche Apps nutzen sie zur Zuordnung Ihrer Playlist, etwa der <a href="/ibo-player/">IBO Player</a>.</dd>
  <dt>Timeshift und Catch-Up</dt><dd>Zurückspulen im Live-Programm beziehungsweise Nachholen einer Sendung. Welche Apps das bieten, steht im <a href="/iptv-apps/">App-Vergleich</a>.</dd>
</dl>
<h2 id="einsteiger-fragen">Drei Einsteigerfragen, kurz beantwortet</h2>
<p><strong>Brauche ich einen Smart-TV?</strong> Nein. Mit einem <a href="/iptv-stick/">Stick</a> oder einer <a href="/iptv-box/">Box</a> läuft IPTV auch auf älteren Fernsehern.</p>
<p><strong>Wie schnell muss das Internet sein?</strong> Für HD genügen rund 16 Mbit/s, für 4K etwa 30 Mbit/s, siehe <a href="/iptv-stream/">IPTV Stream</a>.</p>
<p><strong>Kann ich vorher testen?</strong> Ja, mit dem <a href="/kostenloser-test/">kostenlosen 24-Stunden-Test</a>.</p>
''',
),

"formuler": dict(
    body='''
<h2 id="formuler-faq-ergaenzung">Häufige Fragen zur Einrichtung</h2>
<p>Viele Formuler-Nutzer stolpern an denselben Stellen. Erstens: Der Portal-Link und die Xtream-Daten sind zwei verschiedene Wege, tragen Sie nur einen von beiden ein. Zweitens: Der Programmführer lädt separat und kann beim ersten Start länger dauern; lassen Sie die Box dafür einige Minuten laufen. Drittens: Erscheint die Senderliste nicht, prüfen Sie Datum und Uhrzeit der Box, denn eine falsche Systemzeit verhindert manchmal die Anmeldung. Ist der Zugang bestätigt, aber ein einzelner Sender bleibt schwarz, testen Sie ihn in einer zweiten App, um Zugang und Box zu trennen. Weitere Lösungen sammelt die <a href="/iptv-hilfe/">IPTV Hilfe</a>.</p>
''',
),

"iptv-android": dict(
    body='''
<h2 id="android-sicherheit">Apps sicher installieren</h2>
<p>Installieren Sie IPTV-Apps nur aus dem Store Ihres Geräts oder von der Seite des Entwicklers. Apps aus unbekannten Quellen (APK-Dateien von Foren oder Messenger-Gruppen) können verändert sein. Prüfen Sie nach der Installation, welche Berechtigungen die App verlangt: Ein Player braucht Netzwerkzugriff, aber keinen Zugriff auf Kontakte oder SMS. Wie Sie Ihre Zugangsdaten schützen, steht auf der Seite <a href="/xtream-codes/">Xtream Codes</a>.</p>
''',
),

"ibo-player": dict(
    body='''
<h2 id="ibo-pflege">Playlist pflegen und Fehler vermeiden</h2>
<p>Haben Sie den Zugang gewechselt oder das Passwort geändert, muss die Playlist beim IBO Player aktualisiert werden. Melden Sie sich dafür an der Verwaltungsseite an, ersetzen Sie den Eintrag und starten Sie die App auf dem Fernseher neu. Bleibt die Liste leer, prüfen Sie zuerst MAC-Adresse und Device Key auf Tippfehler. Hilft das nicht, sendet unser Support den Eintrag neu zu. Allgemeine Fehlersuche: <a href="/iptv-hilfe/">IPTV Hilfe</a>.</p>
''',
),

"ss-iptv": dict(
    body='''
<h2 id="ssiptv-sicherheit">Zugangsdaten und Datenschutz</h2>
<p>Der M3U-Link enthält Ihren Benutzernamen und Ihr Passwort. Geben Sie ihn nicht in öffentliche Foren oder Chatgruppen und veröffentlichen Sie keine Screenshots, auf denen er zu lesen ist. Bei einem Verdacht auf Weitergabe melden Sie sich beim Support. Die Datenschutzhinweise unseres Angebots finden Sie in der <a href="/datenschutz">Datenschutzerklärung</a>.</p>
''',
),

"set-iptv": dict(
    body='''
<h2 id="setiptv-vergleich-detail">Set IPTV im Vergleich zu ähnlichen Apps</h2>
<p>Set IPTV, <a href="/smart-one-iptv/">SmartOne</a>, <a href="/flix-iptv/">Flix IPTV</a> und der <a href="/ibo-player/">IBO Player</a> arbeiten nach demselben Prinzip: Die App zeigt die Playlist, die Sie über die MAC-Adresse zuordnen. Unterschiede liegen in Oberfläche, Tempo und Zusatzfunktionen wie Untertiteln oder Elternsperre. Welche App auf Ihrem Fernseher am flüssigsten läuft, merken Sie am besten durch Ausprobieren, denn Ihre Playlist und Ihr Abo bleiben dabei unverändert. Einen Gesamtüberblick bietet der <a href="/iptv-apps/">IPTV Apps Vergleich</a>.</p>
''',
),

"smart-one-iptv": dict(
    body='''
<h2 id="smartone-checkliste">Kurz-Checkliste bei Problemen</h2>
<ol>
  <li>Internetverbindung des Fernsehers prüfen, notfalls per LAN-Kabel.</li>
  <li>MAC-Adresse in der App und im Verwaltungsbereich vergleichen.</li>
  <li>Playlist neu speichern und die App vollständig beenden.</li>
  <li>Fernseher kurz vom Strom trennen.</li>
  <li>Bei anhaltendem Fehler eine andere App testen und den Support kontaktieren.</li>
</ol>
''',
),

"flix-iptv": dict(
    body='''
<h2 id="flix-tipps-alltag">Tipps für den Alltag</h2>
<p>Legen Sie in Flix IPTV eigene Favoritenlisten für Familienmitglieder an, damit Kinder und Erwachsene schneller ihre Sender finden. Aktivieren Sie bei Serien die Anzeige zuletzt gesehener Folgen und prüfen Sie in den Einstellungen die Bevorzugte Tonspur und Untertitelsprache. Nach Änderungen an Playlist oder Zugang hilft ein vollständiger Neustart der App. Bei Fragen zum Zugang selbst ist der Support Ansprechpartner, bei der App-Bedienung die Hilfe der App.</p>
''',
),

"xciptv": dict(
    body='''
<h2 id="xc-probleme">Wenn XCIPTV Sender nicht lädt</h2>
<ul>
  <li><strong>Falsche Server-Adresse:</strong> Sie muss mit http:// oder https:// beginnen und den Port enthalten, wenn ihn Ihr Zugang vorgibt.</li>
  <li><strong>Zu viele Geräte:</strong> Wird der Zugang auf mehr Geräten genutzt, als das Paket erlaubt, bricht die Anmeldung ab.</li>
  <li><strong>Speicher voll:</strong> Auf älteren Fire TV Sticks hilft es, ungenutzte Apps zu löschen und den Cache der App zu leeren.</li>
  <li><strong>Veraltete App:</strong> Aktualisieren Sie XCIPTV, wenn Kategorien leer bleiben.</li>
</ul>
<p>Weitere Lösungen: <a href="/iptv-hilfe/">IPTV Hilfe</a>.</p>
''',
),

"kodi-iptv": dict(
    body='''
<h2 id="kodi-grenzen">Grenzen von Kodi bei IPTV</h2>
<p>Kodi ist ein vielseitiges Mediacenter, aber kein reiner IPTV-Player. Das macht sich bemerkbar: Die Einrichtung dauert länger als bei einer IPTV-App, Filme und Serien aus dem Xtream-Zugang erscheinen nicht automatisch in der Mediathek, und das Umschalten kann je nach Gerät etwas träger sein. Dafür bietet Kodi Skins, Aufnahmefunktionen über das PVR-Backend und Erweiterungen, die eine IPTV-App nicht kennt. Wer vor allem Live-TV schauen will, ist mit einer spezialisierten App schneller am Ziel, siehe <a href="/iptv-apps/">IPTV Apps</a>.</p>
''',
),

"vlc-iptv": dict(
    body='''
<h2 id="vlc-wann">VLC oder IPTV-App?</h2>
<p>VLC ist ideal für den schnellen Test am Rechner oder Handy: Link einfügen, Sender prüfen, fertig. Für den Alltag fehlen Programmführer, Favoriten nach Gruppen, Aufnahme und die Mediathek. Wenn Sie IPTV täglich schauen, wechseln Sie deshalb zu einer Anwendung wie <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a>. Der Zugang bleibt derselbe, nur die Bedienung wird komfortabler. Wie Sie am Rechner starten, zeigt die Seite <a href="/iptv-pc-mac/">IPTV am PC und Mac</a>.</p>
''',
),

"iptv-ex-yu": dict(
    body='''
<h2 id="exyu-geraete">Geräte und Apps für Ex-Yu-Sender</h2>
<p>Auf jedem unterstützten Gerät sehen Sie dieselben Sendergruppen. Beliebt sind der <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> mit TiviMate, Smart-TVs mit dem <a href="/ibo-player/">IBO Player</a> und Android-Handys für unterwegs. Wer eine klassische Box bevorzugt, nutzt eine <a href="/mag-box/">MAG Box</a>.</p>
''',
),

"iptv-albanisch": dict(
    body='''
<h2 id="shqip-geraete">Geräte und Apps</h2>
<p>Albanische Sender laufen auf denselben Geräten wie alle anderen Programme. Smart-TVs von Samsung und LG nutzen den <a href="/ibo-player/">IBO Player</a>, am Fire TV Stick bieten sich <a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> an. Für unterwegs genügt ein Android-Handy mit <a href="/iptv-android/">passender App</a>. In der App legen Sie eine Favoritengruppe „Shqip“ an und erreichen Ihre Sender mit einem Klick.</p>
<h2 id="shqip-programmfuehrer">Programmführer und Qualität</h2>
<p>Der Programmführer ist nicht für jeden Sender in gleicher Tiefe verfügbar. Prüfen Sie im <a href="/kostenloser-test/">Test</a>, ob Ihre Wunschsender Sendungsinformationen anzeigen. Bei der Bildqualität gilt: Läuft ein Sender nur in SD, liegt das an der Quelle und nicht an Ihrer Leitung.</p>
''',
),

"iptv-rumaenisch": dict(
    body='''
<h2 id="ro-geraete">Geräte und Apps</h2>
<p>Rumänische Sender schauen Sie auf Smart-TV, <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, Handy und Tablet. Die Sender liegen in einer eigenen Gruppe; legen Sie in der App eine Favoritenliste „România“ an. Ein <a href="/tivimate/">TiviMate</a>-Profil pro Familienmitglied hält Listen getrennt. Auf Samsung und LG ist der <a href="/ibo-player/">IBO Player</a> die erste Wahl.</p>
<h2 id="ro-programmfuehrer">Programmführer und Qualität</h2>
<p>Nicht für jeden Sender liegt ein Programmführer vor. Prüfen Sie im Test, ob die Sendungsinfos Ihrer Lieblingssender angezeigt werden. Die Bildqualität richtet sich nach der Quelle des Senders; Sport und Nachrichten laufen häufig in HD.</p>
''',
),

"iptv-russisch": dict(
    body='''
<h2 id="ru-geraete">Geräte und Apps</h2>
<p>Russischsprachige Programme laufen auf Smart-TV, <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, Android-Box und Handy. Die Gruppe finden Sie in der Senderliste Ihrer App; für schnellen Zugriff legen Sie eine Favoritenliste an. Kyrillische Zeichen werden angezeigt, sofern die App sie unterstützt, was bei aktuellen Versionen von <a href="/tivimate/">TiviMate</a> und <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> der Fall ist.</p>
<h2 id="ru-hinweis">Hinweis zu Verfügbarkeit</h2>
<p>Einzelne Programme sind aus rechtlichen Gründen nicht verfügbar. Fragen Sie vor der Bestellung nach Ihren Wunschsendern oder prüfen Sie die Liste im <a href="/kostenloser-test/">kostenlosen Test</a>.</p>
''',
),

"iptv-georgien": dict(
    body='''
<h2 id="ge-qualitaet">Qualität und Programmführer</h2>
<p>Bild- und Tonqualität hängen vom Sender ab: Nachrichten und Sport laufen häufig in HD, ältere Archivprogramme teils in SD. Programminformationen sind nicht für jeden georgischen Sender verfügbar; prüfen Sie im Test, ob Ihre Sender Sendungsinfos zeigen. Bei Aussetzern helfen die Tipps der <a href="/iptv-hilfe/">IPTV Hilfe</a>, zum Beispiel LAN-Kabel statt WLAN.</p>
''',
),
}
