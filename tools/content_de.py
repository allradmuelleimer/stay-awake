"""Deutsche Texte. Anrede "du" wie in der App. Fakten nur aus der App (siehe build.py).

Suchanfragen, auf die die Anleitungen zielen (Google-Vorschlaege, 21.11.2026):
- wach bleiben nachtschicht / tipps wach bleiben nachtschicht
- wach bleiben beim lernen / wie bleibe ich wach in der schule
- die ganze nacht wach bleiben / ganze nacht wach bleiben tipps / wie bleibe ich nachts wach
- wie bleibe ich wach ohne koffein / wach bleiben ohne kaffee
- intervall wecker / intervall wecker app / wecker alle 30 minuten / samsung wecker intervall
- Wecker, der prueft, ob man wach ist (keine Vorschlaege, aber der Kern der App)
- android wecker klingelt nicht (+ nach update, bei lautlos, wenn handy aus, manchmal)

Verboten in allen Texten: Autofahren/Strassenverkehr, Arbeitsschutz-Versprechen, "verhindert
Einschlafen", medizinische Ratschlaege. Einzige Erwaehnung des Fahrens ist der Satz zu den
Grenzen auf der Startseite, wortgleich mit dem Play-Eintrag.
"""

APP = "Stay Awake"

C = {
    "app_name": APP,
    "lang_name": "Deutsch",
    "og_locale": "de_DE",
    "ui": {
        "skip": "Zum Inhalt springen",
        "nav": "Hauptnavigation",
        "guides": "Anleitungen",
        "privacy": "Datenschutz",
        "imprint": "Impressum",
        "faq": "Häufige Fragen",
        "toc": "Inhalt",
        "crumbs": "Brotkrumen",
        "updated": "Stand:",
        "with_app": "Mit der App",
        "more_guides": "Weitere Anleitungen",
        "play_cta": "Bei Google Play laden",
        "play_note": "Kostenlos für Android · ohne Konto",
        "footer_tag": "Wach-Check-Timer für Android.",
        "trademark": "Google Play und Android sind Marken von Google LLC.",
    },

    # ------------------------------------------------------------ Startseite
    "home": {
        "title": "Stay Awake – der Wecker, der immer wieder fragt, ob du noch wach bist",
        "desc": "Ein Wecker klingelt einmal, du machst ihn aus und schläfst wieder ein. Stay Awake fragt immer wieder, ob du noch wach bist – und klingelt, bis du antwortest.",
        "kicker": "Für alle, die wach bleiben müssen",
        "h1": "Ein Wecker klingelt einmal. Stay Awake fragt immer wieder.",
        "lead": "Kennst du das: Der Wecker klingelt, du machst ihn aus – und fünf Minuten später schläfst du wieder. Stay Awake hört nach einem Klingeln nicht auf. Alle 30 Minuten, oder in deinem Takt, fragt die App: **Bist du noch wach?** Einmal schütteln oder tippen, und die nächste Runde beginnt. Keine Antwort? Nach 10 Sekunden vibriert das Telefon, nach 20 klingelt ein Alarm – so lange, bis du antwortest.",
        "who": "Nachtschicht · Bereitschaft · Lernnächte · durch die Nacht warten",
        "why_h2": "Warum ein normaler Wecker nicht reicht",
        "why_lead": "Ein Wecker ist dafür gebaut, dich einmal zu wecken. Wach bleiben heißt aber, Stunde um Stunde durchzuhalten – und schwierig ist genau der Moment, in dem niemand nachfragt.",
        "why": [["Normaler Wecker", ["Klingelt einmal – zu einer Uhrzeit, die du vorher festlegst.", "Im Halbschlaf ausgemacht, und danach kommt nichts mehr.", "Fragt nie, ob du noch wach bist."]], ["Stay Awake", ["Fragt immer wieder, die ganze Nacht – in deinem Takt, von einer Minute bis zwölf Stunden.", "Fragt erst leise. Nur ohne Antwort vibriert es, dann klingelt es.", "Der Alarm klingelt, bis du antwortest. Dann beginnt die nächste Runde."]]],
        "hero_shot": "de-session.webp",
        "shots": {
            "de-session.webp": "Laufende Sitzung: ein Amber-Ring um den Countdown 29:50, darunter „bis zum nächsten Check“, „Unbegrenzt“, „Alle 30 Minuten · Tippen oder Schütteln“, der Knopf „Ich bin wach“ und „Sitzung beenden“.",
            "de-home.webp": "Startbildschirm: Unbegrenzt oder Timer, ein runder Regler auf 30 Minuten und der Knopf Sitzung starten.",
            "de-check.webp": "Der Check: „Bist du noch wach?“, darunter „oder Handy schütteln“, eine dünne Fortschrittslinie und ein großer Ja-Knopf, darunter Sitzung beenden.",
            "de-alarm.webp": "Nach 20 Sekunden ohne Antwort: derselbe Check, jetzt mit „Check verpasst“ und roter Linie. Der Alarm läuft.",
            "de-schedules.webp": "Zeitpläne: 22:00 – 06:00, Montag bis Freitag, alle 30 Minuten, eingeschaltet.",
            "de-reliability.webp": "Verlässlichkeit: „Bereit“ mit neun grünen Punkten – Benachrichtigungen, Check- und Alarm-Meldungen, pünktliches Wecken, über dem Sperrbildschirm, Wecker-Lautstärke, Nicht stören, Vibration, Hintergrund und Akku, gewählte Aktionen.",
            "de-timer.webp": "Timer: Für 2:00 Std., Check-Intervall 30 Minuten.",
            "de-settings.webp": "Einstellungen: Tippen auf „Ja“ funktioniert immer; zusätzlich Handy schütteln, Handy umdrehen oder Lautstärketaste.",
        },
        "steps_h2": "Was passiert, wenn ein Check fällig ist",
        "steps_lead": "Erst leise, laut nur wenn nötig. Jede Stufe endet in dem Moment, in dem du antwortest.",
        "steps": [
            ["0 s", "Die Frage", "Der Bildschirm geht an – auch über dem Sperrbildschirm – und fragt: Bist du noch wach?"],
            ["10 s", "Vibration", "Noch keine Antwort? Das Telefon beginnt zu vibrieren."],
            ["20 s", "Alarm", "Immer noch nichts: ein echter Alarm mit dem Weckton deines Telefons."],
            ["Ja", "Nächste Runde", "Ein Tippen oder einmal Schütteln: Alles verstummt, das volle Intervall beginnt neu."],
        ],
        "features_h2": "Starten, bestätigen, planen, prüfen",
        "features": [
            {"kicker": "Starten", "h2": "Zwei Entscheidungen, ein Knopf",
             "body": ["Unbegrenzt oder Timer – und wie oft du gefragt werden willst. Dreh am Regler: von einer Minute bis zu zwölf Stunden, am Anfang 30 Minuten. Die App merkt sich deine letzte Wahl.",
                      "Der Timer läuft eine feste Zeit („für 2 Stunden“) oder bis zu einer Uhrzeit („bis 5:30“)."],
             "shot": "de-home.webp"},
            {"kicker": "Bestätigen", "h2": "Tippen, schütteln, umdrehen – wie du willst",
             "body": ["Das große **Ja** geht immer. In den Einstellungen kannst du Schütteln, Umdrehen (Display nach unten und zurück) und die Lautstärketaste dazunehmen, in jeder Kombination. Schütteln und Umdrehen wirken auch bei dunklem Bildschirm.",
                      "Du musst nicht auf die Frage warten: Bestätige, wann du willst – das Intervall beginnt ab diesem Moment neu. Auch die Benachrichtigung der laufenden Sitzung hat einen Knopf **Ich bin wach**."],
             "shot": "de-check.webp"},
            {"kicker": "Schichten", "h2": "Zeitpläne, die von selbst starten",
             "body": ["Für Nächte, die sich wiederholen: Beginn, Ende, auf Wunsch Wochentage, Intervall. Die Sitzung startet zur eingestellten Zeit von selbst und endet zur Endzeit.",
                      "Ohne Wochentag läuft der Zeitplan einmal, beim nächsten Start."],
             "shot": "de-schedules.webp"},
            {"kicker": "Verlässlichkeit", "h2": "Weiß, was dein Telefon zulässt",
             "body": ["Android-Telefone können Alarme zurückhalten – Akkusparen, Nicht stören, fehlende Berechtigungen. Die Verlässlichkeitsprüfung geht jeden Punkt in klaren Worten durch und zeigt, wie du behebst, was nicht passt.",
                      "Mit **Alarm testen** hörst und spürst du den Alarm fünf Sekunden lang, bevor die erste echte Nacht kommt."],
             "shot": "de-reliability.webp"},
        ],
        "limits_h2": "Ehrliche Grenzen",
        "limits": "Stay Awake hilft dir, wach zu bleiben. Die App ersetzt weder Schlaf noch Pausen und ist kein Sicherheitssystem für Arbeit oder Straßenverkehr. Ob ein Check pünktlich kommt, hängt auch vom Telefon ab – die Verlässlichkeitsprüfung zeigt, was deines zulässt.",
        "nots_h2": "Nichts, wofür du dich anmelden musst",
        "nots": [
            "**Kein Konto, keine Anmeldung.** Sitzungen, Zeitpläne und Einstellungen bleiben auf deinem Telefon.",
            "**Funktioniert offline.** Checks und Alarm brauchen kein Internet.",
            "**Sitzungen überstehen einen Neustart** des Telefons.",
            "**Kostenlos mit kleinem Banner.** Keine Werbung auf dem Check und beim Alarm. Stay Awake Pro entfernt den Banner – monatlich oder als Einmalkauf.",
            "**20 Sprachen**, von Arabisch bis Vietnamesisch.",
        ],
        "privacy_link": "Datenschutzerklärung lesen",
        "guides_h2": "Anleitungen für lange Nächte",
        "guides_lead": "Auch ohne App nützlich: Nachtschicht, Lernen bis spät, wach bleiben ohne Kaffee, Intervall-Wecker.",
        "faq": [
            ["Was ist der Unterschied zu einem normalen Wecker?",
             ["Ein Wecker klingelt zu einer Uhrzeit, egal ob du wach bist. Stay Awake fragt erst und wird nur laut, wenn keine Antwort kommt. Die App ist zum Wachbleiben gemacht, nicht zum Aufwachen am Morgen."]],
            ["Muss der Bildschirm anbleiben?",
             ["Nein. Leg das Telefon hin, sperr es, lass den Bildschirm dunkel werden. Der Check erscheint über dem Sperrbildschirm. Hast du Schütteln gewählt, bestätigt ein Schütteln auch bei dunklem Bildschirm."]],
            ["Welcher Ton klingelt?",
             ["Voreingestellt der Weckton deines Telefons – der, auf den du ohnehin reagierst. In den Einstellungen kannst du die Stay-Awake-Melodie oder einen anderen Ton wählen."]],
            ["Funktioniert die App ohne Internet?",
             ["Ja. Checks, Vibration und Alarm laufen vollständig auf dem Telefon."]],
            ["Was kostet die App?",
             ["Alles, was dich wach hält, ist kostenlos. Die kostenlose Version zeigt einen kleinen Banner auf den normalen Bildschirmen, nie auf dem Check oder beim Alarm. Stay Awake Pro entfernt ihn, monatlich oder einmalig; den Preis zeigt Google Play."]],
            ["Gibt es Stay Awake fürs iPhone?",
             ["Nein, Stay Awake gibt es nur für Android."]],
        ],
        "final_h2": "Wenn du wach bleiben musst, ist das deine App.",
        "final_body": "Sitzung starten, Handy weglegen. Stay Awake fragt weiter, bis du die Sitzung beendest.",
    },

    "guides_index": {
        "title": "Anleitungen: wach bleiben in der Nacht, in der Schicht, beim Lernen",
        "desc": "Praktische Anleitungen für lange Nächte: Nachtschicht, Lernen bis spät, wach bleiben ohne Kaffee, Wecker alle 30 Minuten und Android-Wecker, die nicht klingeln.",
        "h1": "Anleitungen für lange Nächte",
        "lead": "Kurze, praktische Antworten – jede auch ohne App nützlich.",
        "app": "**Stay Awake** fragt in deinem Takt, ob du noch wach bist, und schlägt Alarm, wenn keine Antwort kommt.",
    },

    # ------------------------------------------------------------ Anleitungen
    "guides": [
        {
            "id": "nightshift",
            "slug": "wach-bleiben-nachtschicht",
            "title": "Wach bleiben in der Nachtschicht: 9 praktische Tipps",
            "desc": "Wach durch die Nachtschicht: Licht, Bewegung, kleine Aufgaben für das Tief gegen 3 Uhr, Essen und ein fester Takt zum Einchecken. Praktisch, ohne Tricks.",
            "h1": "Wach bleiben in der Nachtschicht",
            "teaser": "Licht, Bewegung und ein Plan für das Tief gegen 3 Uhr.",
            "answer": "Schwierig ist in der Nachtschicht selten der Anfang – sondern die stille Strecke in den frühen Morgenstunden, in der nichts passiert. Am meisten helfen **Licht, Bewegung und ein Takt**: Teil die Nacht in kurze Abschnitte, gib jedem etwas zu tun und sitz nicht lange still im Halbdunkel.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["tief", "Plane das Tief ein", [
                    "Wer nachts arbeitet, kennt den Moment: Irgendwann zwischen 2 und 5 Uhr wird es ruhig, der Kaffee wirkt nicht mehr und die Augen werden schwer. Überlass diese Strecke nicht dem Zufall.",
                    {"list": [
                        "**Heb aktive Aufgaben dafür auf.** Auffüllen, Ablage, Rundgang, Geräte prüfen – alles, wofür du aufstehen und gehen musst.",
                        "**Teil die Nacht in Abschnitte** von 30 bis 60 Minuten. Jeder endet mit einer kleinen Handlung: aufstehen, Wasser trinken, eine Zeile ins Protokoll.",
                        "**Vermeide lange passive Phasen** wie Lesen oder Bildschirmschauen tief im Sessel.",
                    ]},
                ]],
                ["tipps", "9 Tipps, die vielen helfen", [
                    {"steps": [
                        "**Mach es hell.** Halbdunkel macht schläfrig. Schalte das Hauptlicht ein statt nur einer Lampe, wo dein Arbeitsplatz es zulässt.",
                        "**Beweg dich jede halbe Stunde.** Den Flur entlang, ein paar Treppen, Dehnen – wenige Minuten reichen.",
                        "**Steh bei Routinearbeit.** Im Sitzen nickt man leicht weg.",
                        "**Trink regelmäßig Wasser.** Das gibt dir auch einen Grund aufzustehen.",
                        "**Iss kleine Portionen.** Nach einer großen Mahlzeit mitten in der Nacht fühlen sich viele träge; mehrere kleine Snacks sind leichter.",
                        "**Nutz kaltes Wasser.** Ins Gesicht oder über die Hände, wenn die Schwere kommt.",
                        "**Sprich mit jemandem.** Ein kurzes Gespräch mit Kollegen unterbricht die stille Strecke – für dich und für sie.",
                        "**Frische Luft.** Ein paar Minuten am offenen Fenster oder draußen.",
                        "**Check zu festen Zeiten ein.** Eine regelmäßige Erinnerung – alle 20 oder 30 Minuten –, die eine bewusste Antwort verlangt, hilft dir zu merken, wenn aus Minuten unbemerkt eine Stunde zu werden droht.",
                    ]},
                ]],
                ["vorher", "Vor und nach der Schicht", [
                    "Eine Nachtschicht beginnt früher, als die Uhr sagt: Wer schon müde ankommt, den trägt kein Tipp durch. Plane deinen Schlaf vor der ersten Nacht und schütze ihn nach der Schicht – dunkles Zimmer, Handy lautlos, Mitbewohner eingeweiht.",
                    {"note": "Wenn du merkst, dass du immer wieder wegnickst, ist das ein Signal, das du ernst nehmen solltest. Sprich mit deinem Team oder deinem Arbeitgeber – keine App und kein Tipp ersetzt Schlaf."},
                ]],
            ],
            "app": {
                "h2": "Alle 30 Minuten ein Check-in",
                "body": [
                    "Stay Awake macht aus Tipp 9 eine Routine: Die App fragt in deinem Takt, ob du noch wach bist. Handy schütteln oder Ja tippen, und die nächste Runde beginnt. Antwortest du nicht, vibriert es nach 10 Sekunden, nach 20 ertönt ein Alarm.",
                    "Für wiederkehrende Schichten legst du einen **Zeitplan** an – etwa 22 bis 6 Uhr, Montag bis Freitag. Dann startet und endet die Sitzung von selbst.",
                ],
                "shot": "de-schedules.webp",
                "alt": "Zeitplan 22:00 – 06:00, Montag bis Freitag, alle 30 Minuten.",
            },
            "faq": [
                ["Wann ist es in der Nachtschicht am schwersten, wach zu bleiben?",
                 ["Für viele in den frühen Morgenstunden, etwa zwischen 2 und 5 Uhr. Leg aktive Aufgaben in diese Zeit."]],
                ["Hilft Kaffee in der Nachtschicht?",
                 ["Viele trinken zu Schichtbeginn Kaffee. Er ersetzt aber weder Licht noch Bewegung noch einen Takt – und wie viel für dich richtig ist, kann dir keine Website sagen."]],
                ["Wie bleibe ich in einer ruhigen Nacht wach, in der nichts zu tun ist?",
                 ["Gib dir alle 30 bis 60 Minuten kleine feste Aufgaben, steh regelmäßig auf und halte den Raum hell. Eine regelmäßige Erinnerung zum Einchecken hilft dir zu merken, wann du abdriftest."]],
            ],
        },
        {
            "id": "study",
            "slug": "wach-bleiben-beim-lernen",
            "title": "Wach bleiben beim Lernen – auch spät abends",
            "desc": "Lernen bis spät, ohne über den Unterlagen einzuschlafen: in kurzen Blöcken arbeiten, aktiv lernen, Raum hell halten und einen Check-in-Timer nutzen.",
            "h1": "Wach bleiben beim Lernen",
            "teaser": "Kurze Blöcke, aktives Lernen und ein Timer, der nachfragt.",
            "answer": "Lesen ist der schnellste Weg, über den Unterlagen einzuschlafen. Länger wach bleibst du, wenn du **aktiv und in kurzen Blöcken** lernst: schreiben, erklären, dich abfragen – und zwischen den Blöcken aufstehen.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["aktiv", "Aktiv lernen statt lesen", [
                    "Die Augen können über eine Seite wandern, während der Kopf längst abgeschaltet hat. Aktive Methoden halten dich beschäftigt:",
                    {"list": [
                        "**Frag dich ab**, statt noch einmal zu lesen: Seite abdecken, aufschreiben, was du weißt, dann vergleichen.",
                        "**Erklär es laut**, als säße jemand neben dir.",
                        "**Schreib mit der Hand** – Zusammenfassungen, Mindmaps, Karteikarten.",
                        "**Rechne Aufgaben selbst**, statt die Lösungen zu lesen.",
                    ]},
                ]],
                ["bloecke", "In Blöcken arbeiten", [
                    "Leg einen festen Takt fest, zum Beispiel 25 bis 50 Minuten lernen und fünf Minuten Pause. In der Pause stehst du auf: gehen, dehnen, Wasser holen, Fenster auf. Verbring die Pause nicht auf dem Bett – so wird aus fünf Minuten Pause ein Schlaf von zwei Stunden.",
                    {"table": [
                        ["Zeit", "Block"],
                        ["22:00 – 22:45", "Übungsaufgaben Kapitel 4"],
                        ["22:45 – 22:50", "Aufstehen, Wasser, Fenster auf"],
                        ["22:50 – 23:35", "Karteikarten Kapitel 4, selbst abfragen"],
                        ["23:35 – 23:40", "Kurz durch die Wohnung gehen"],
                    ]},
                ]],
                ["raum", "Den Raum einrichten", [
                    {"list": [
                        "**Helles Licht** am Schreibtisch und im Raum, nicht nur eine Leselampe.",
                        "**Am Schreibtisch sitzen**, nicht auf Bett oder Sofa.",
                        "**Eher kühl als warm** – stickige Luft macht schläfrig.",
                        "**Handy außer Reichweite**, außer als Timer.",
                    ]},
                ]],
                ["grenze", "Wann Schluss ist", [
                    "Wenn du denselben Absatz zum dritten Mal liest, hat die Nacht meist gebracht, was sie bringen kann. Was du im Halbschlaf lernst, bleibt selten hängen. Manchmal ist schlafen und früh anfangen der bessere Plan.",
                ]],
            ],
            "app": {
                "h2": "Ein Timer, der nachfragt",
                "body": [
                    "Ein normaler Timer klingelt, wenn der Block vorbei ist – auch wenn du schon zehn Minuten vorher über den Unterlagen eingeschlafen bist. Stay Awake fragt in deinem Takt, ob du noch wach bist. Handy schütteln oder Ja tippen, und es geht weiter. Keine Antwort: Vibration nach 10 Sekunden, Alarm nach 20.",
                    "Mit dem **Timer** legst du fest, wie lange die Sitzung läuft, etwa „für 3 Stunden“ oder „bis 1:00“.",
                ],
                "shot": "de-timer.webp",
                "alt": "Timer: Für 2:00 Std., Check-Intervall 30 Minuten, Sitzung starten.",
            },
            "faq": [
                ["Wie lang sollte ein Lernblock abends sein?",
                 ["Viele kommen mit 25 bis 50 Minuten und einer kurzen Pause gut zurecht. Probier aus, was zu dir passt – wichtig ist, dass du in der Pause aufstehst."]],
                ["Lieber spät lernen oder früh aufstehen?",
                 ["Das hängt von dir ab. Wenn du merkst, dass nichts mehr hängen bleibt, ist schlafen und morgens weiterlernen oft ergiebiger."]],
                ["Wie schlafe ich beim Lesen nicht ein?",
                 ["Mach aus dem Lesen eine aktive Aufgabe: Notizen machen, dir Fragen stellen, den Inhalt laut erklären. Und sitz bei hellem Licht am Schreibtisch."]],
            ],
        },
        {
            "id": "allnight",
            "slug": "die-ganze-nacht-wach-bleiben",
            "title": "Die ganze Nacht wach bleiben – Tipps und ein Plan",
            "desc": "Wenn du die ganze Nacht durchmachen musst: ein Plan für Abend, Mitternacht, das Tief und den Morgen – und wie du merkst, falls du doch wegnickst.",
            "h1": "Die ganze Nacht wach bleiben",
            "teaser": "Ein Plan für Abend, Mitternacht, das Tief und den Morgen.",
            "answer": "Eine ganze Nacht gelingt besser mit Plan als mit Willenskraft. Fang möglichst ausgeruht an, halte es **hell und aktiv**, gib den Stunden nach 2 Uhr die aktivsten Aufgaben – und sorg für etwas, das regelmäßig **nachfragt** und laut wird, wenn keine Antwort kommt.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["plan", "Ein Plan für die Nacht", [
                    {"table": [
                        ["Wann", "Was hilft"],
                        ["Abend", "Wenn möglich ausgeruht anfangen. Normal essen, spät nichts Schweres."],
                        ["Bis Mitternacht", "Jetzt die Arbeit, die den klarsten Kopf braucht."],
                        ["Mitternacht bis 2 Uhr", "In Blöcken arbeiten, dazwischen aufstehen und bewegen."],
                        ["2 bis 5 Uhr", "Für viele die schwerste Strecke: aktive Aufgaben, helles Licht, frische Luft."],
                        ["Morgen", "Tageslicht hilft vielen über die letzte Strecke. Nichts tun, was volle Konzentration braucht."],
                    ]},
                ]],
                ["was-hilft", "Was dich trägt", [
                    {"list": [
                        "**Licht:** Hauptlicht an, Bildschirm hell genug.",
                        "**Bewegung:** jede halbe Stunde ein paar Minuten.",
                        "**Kaltes Wasser** auf Gesicht und Hände.",
                        "**Etwas für die Hände** statt passivem Zuschauen.",
                        "**Gesellschaft:** ein Anruf oder Chat mit jemandem, der auch wach ist.",
                    ]},
                ]],
                ["merken", "Merken, wenn du wegnickst", [
                    "Die Gefahr einer langen Nacht ist nicht der große Zusammenbruch, sondern die kleinen Momente: Augen zu, „nur kurz“ – und plötzlich ist es eine Stunde später. Das merkst du nur, wenn dich etwas von außen fragt.",
                    "Ohne App: ein Timer, den du nach jedem Klingeln neu startest, oder jemand, der sich regelmäßig per Nachricht meldet. Mit App: siehe unten.",
                ]],
                ["danach", "Der Tag danach", [
                    "Eine Nacht ohne Schlaf holt dich ein. Plan den nächsten Tag leicht und hol den Schlaf so bald wie möglich nach.",
                    {"note": "Ob es für dich eine gute Idee ist, die Nacht durchzumachen, kannst nur du – oder eine Ärztin, ein Arzt – beurteilen. Hier geht es darum, durch eine Nacht zu kommen, für die du dich schon entschieden hast."},
                ]],
            ],
            "app": {
                "h2": "Jemand, der alle 30 Minuten fragt",
                "body": [
                    "Stay Awake fragt in deinem Takt, ob du noch wach bist. Einmal schütteln oder tippen, und die nächste Runde beginnt. Bleibt die Antwort aus, vibriert das Telefon nach 10 Sekunden, nach 20 ertönt ein Alarm – mit dem Weckton deines Telefons.",
                    "Starte eine **unbegrenzte** Sitzung für eine Nacht mit offenem Ende oder einen **Timer** „bis 6:00“.",
                ],
                "shot": "de-alarm.webp",
                "alt": "Check nach 20 Sekunden: Check verpasst, Bist du noch wach?, großer Ja-Knopf.",
            },
            "faq": [
                ["Wann ist es am schwersten, wach zu bleiben?",
                 ["Viele empfinden die Zeit zwischen etwa 2 und 5 Uhr als die schwerste. Heb dir die aktivsten Aufgaben dafür auf."]],
                ["Hilft ein kurzes Nickerchen?",
                 ["Manche planen ein kurzes Nickerchen ein. Das Risiko: Man schläft viel länger als gedacht. Wenn du es machst, stell einen Wecker, den du nicht überhören kannst."]],
                ["Wie stelle ich sicher, dass ich aufwache, falls ich wegnicke?",
                 ["Mit etwas, das regelmäßig nachfragt und laut wird, wenn du nicht reagierst – eine andere Person, ein wiederholter Timer oder eine Wach-Check-App."]],
            ],
        },
        {
            "id": "nocaffeine",
            "slug": "wach-bleiben-ohne-kaffee",
            "title": "Wach bleiben ohne Kaffee und Koffein: 10 Wege",
            "desc": "Wach bleiben ohne Kaffee oder Energydrinks: Licht, Kälte, Bewegung, Haltung, Gespräche, Kauen und ein fester Takt. Einfache Wege für heute Nacht.",
            "h1": "Wach bleiben ohne Kaffee",
            "teaser": "Licht, Kälte, Bewegung und Takt statt Koffein.",
            "answer": "Ohne Koffein brauchst du andere Signale: **helles Licht, kühle Luft, Bewegung und etwas zu tun.** Nichts davon wirkt Wunder, und jedes Signal hält nur kurz – darum zählt am Ende der **Takt**, in dem du sie wiederholst.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["zehn", "10 Wege zum Ausprobieren", [
                    {"steps": [
                        "**Helles Licht.** Hauptlicht an; morgens ins Tageslicht.",
                        "**Kühle Luft.** Fenster auf, Heizung etwas runter.",
                        "**Kaltes Wasser** auf Gesicht, Handgelenke und Nacken.",
                        "**Aufstehen.** Eine Weile im Stehen arbeiten, an Theke oder Regal.",
                        "**Kurz bewegen.** Treppe, einmal um den Block, ein paar Kniebeugen.",
                        "**Aufrecht sitzen**, Füße auf dem Boden – nicht eingerollt auf dem Sofa.",
                        "**Etwas kauen:** Kaugummi, einen Apfel, Rohkost.",
                        "**Reden.** Ein Anruf, ein Gespräch, etwas laut erklären.",
                        "**Musik mit Takt**, wenn die Umgebung es zulässt.",
                        "**Aufgabe wechseln**, wenn eine dich schläfrig macht.",
                    ]},
                ]],
                ["takt", "Takt schlägt Willenskraft", [
                    "Jeder dieser Wege wirkt ein paar Minuten. Was dich über Stunden trägt, ist ein Takt: alle 20 bis 30 Minuten eine kleine Handlung, die das Abdriften unterbricht. Lass ihn von außen vorgeben – Timer, Termin, Erinnerung –, denn je müder du bist, desto weniger merkst du, wie die Zeit vergeht.",
                ]],
                ["ehrlich", "Ehrlich gesagt", [
                    "Nichts ersetzt Schlaf. Wenn du so müde bist, dass nichts davon hilft, sagt dir dein Körper etwas – und die beste Entscheidung ist vielleicht, zu schlafen.",
                ]],
            ],
            "app": {
                "h2": "Eine Erinnerung, die eine Antwort will",
                "body": [
                    "Stay Awake gibt dir den Takt ohne Kaffee: In deinem Intervall fragt die App, ob du noch wach bist. Als Antwort reicht ein Schütteln des Handys – das bewegt dich auch ein bisschen. Keine Antwort: Vibration nach 10 Sekunden, Alarm nach 20.",
                ],
                "shot": "de-check.webp",
                "alt": "Check: Bist du noch wach?, oder Handy schütteln, großer Ja-Knopf.",
            },
            "faq": [
                ["Wie werde ich ohne Kaffee am schnellsten wach?",
                 ["Vielen hilft: aufstehen, kaltes Wasser ins Gesicht, ein paar Minuten frische Luft oder Bewegung."]],
                ["Sind Energydrinks koffeinfrei?",
                 ["Nein, die meisten Energydrinks enthalten Koffein. Ein Blick aufs Etikett hilft."]],
                ["Warum werde ich nach ein paar Minuten wieder müde?",
                 ["Die meisten dieser Wege wirken nur kurz. Darum hilft ein regelmäßiger Takt kleiner Unterbrechungen mehr als eine große Anstrengung."]],
            ],
        },
        {
            "id": "every30",
            "slug": "wecker-alle-30-minuten-android",
            "title": "Wecker alle 30 Minuten auf Android: Intervall-Wecker einstellen",
            "desc": "Die Uhr-App von Android kennt kein „alle 30 Minuten“. Drei Wege, die funktionieren: mehrere Wecker, ein neu gestarteter Timer oder ein Intervall-Wecker.",
            "h1": "Wecker alle 30 Minuten auf Android",
            "teaser": "Mehrere Wecker, ein Timer oder ein Intervall-Wecker – drei Wege.",
            "answer": "Die Uhr-Apps der meisten Android-Telefone wiederholen einen Wecker nur **nach Wochentagen**, nicht alle X Minuten. Du hast drei Möglichkeiten: **mehrere Wecker anlegen**, **einen Timer jedes Mal neu starten** oder eine **Intervall-Wecker-App** nutzen.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["mehrere", "Weg 1: mehrere Wecker", [
                    "Leg in der Uhr-App für jede halbe Stunde einen eigenen Wecker an. Für einen Abend geht das, für eine ganze Nacht wird es lang:",
                    {"table": [
                        ["Zeitraum", "Intervall", "Wecker nötig"],
                        ["2 Stunden", "30 Min.", "4"],
                        ["8 Stunden (22–6 Uhr)", "30 Min.", "16"],
                        ["8 Stunden", "15 Min.", "32"],
                    ]},
                    "Nachteile: viel Tipparbeit, und die Wecker klingeln zu festen Zeiten, auch wenn du hellwach bist. Danach musst du alle wieder ausschalten.",
                ]],
                ["timer", "Weg 2: Timer neu starten", [
                    {"steps": [
                        "Öffne die Uhr-App und geh zu **Timer**.",
                        "Stell **30:00** ein und starte.",
                        "Wenn er klingelt, stopp ihn und starte ihn erneut.",
                    ]},
                    "Einfach, aber du musst jedes Mal neu starten. Vergisst du es einmal, passiert für den Rest der Nacht nichts mehr.",
                ]],
                ["app", "Weg 3: eine Intervall-Wecker-App", [
                    "Intervall-Wecker wiederholen sich von selbst. Bevor du dich für einen entscheidest, prüf drei Dinge:",
                    {"list": [
                        "**Klingelt er bei dunklem Bildschirm und gesperrtem Telefon?** Viele Apps funktionieren nur im Vordergrund.",
                        "**Nutzt er exakte Alarme?** Sonst kann Android ihn im Energiesparmodus verzögern.",
                        "**Was passiert, wenn du nicht reagierst?** Ein einfacher Wiederholungswecker klingelt eine Weile und hört dann auf.",
                    ]},
                ]],
            ],
            "app": {
                "h2": "Ein Intervall-Wecker, der erst fragt",
                "body": [
                    "Stay Awake wiederholt sich in deinem Intervall – jeder Wert von einer Minute bis zwölf Stunden – und nutzt exakte Alarme. Die App klingelt nicht sofort los: Erst fragt sie leise, ob du noch wach bist. Antwortest du, beginnt das Intervall ab diesem Moment neu. Keine Antwort: Vibration nach 10 Sekunden, Alarm nach 20.",
                    "So wirst du nicht geweckt, wenn du wach bist – und nicht allein gelassen, wenn nicht.",
                ],
                "shot": "de-home.webp",
                "alt": "Regler auf 30 Minuten, Unbegrenzt oder Timer, Sitzung starten.",
            },
            "faq": [
                ["Kann die Android-Uhr einen Wecker alle 30 Minuten wiederholen?",
                 ["Die Uhr-Apps der meisten Android-Telefone wiederholen Wecker nur nach Wochentagen. Für alle 30 Minuten brauchst du mehrere Wecker, einen Timer oder eine eigene App."]],
                ["Warum klingelt mein Intervall-Wecker bei dunklem Bildschirm nicht?",
                 ["Oft sind Akku-Optimierung oder eine fehlende Berechtigung für exakte Alarme schuld. Siehe [Android-Wecker klingelt nicht](/de/anleitungen/android-wecker-klingelt-nicht/)."]],
                ["Geht auch ein Intervall von 15 oder 45 Minuten?",
                 ["In Stay Awake ja: Der Regler reicht von einer Minute bis zu zwölf Stunden."]],
            ],
        },
        {
            "id": "wakecheck",
            "slug": "wecker-der-prueft-ob-du-wach-bist",
            "title": "Ein Wecker, der prüft, ob du noch wach bist – so funktioniert’s",
            "desc": "Ein Wach-Check fragt in festen Abständen, ob du noch wach bist, und schlägt nur ohne Antwort Alarm. Der Unterschied zum normalen Wecker und wann er hilft.",
            "h1": "Ein Wecker, der prüft, ob du noch wach bist",
            "teaser": "Erst fragen, nur bei Bedarf laut – die Idee hinter dem Wach-Check.",
            "answer": "Ein normaler Wecker klingelt zu einer festen Uhrzeit. Ein **Wach-Check** fragt in festen Abständen, ob du noch wach bist – und wird nur laut, wenn keine Antwort kommt. Du bestätigst mit einem Tippen oder einer Bewegung, dann beginnt das nächste Intervall.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["unterschied", "Wecker, Intervall-Wecker, Wach-Check", [
                    {"table": [
                        ["", "Wecker", "Intervall-Wecker", "Wach-Check"],
                        ["Klingelt", "Zur festen Uhrzeit", "Alle X Minuten", "Nur ohne Antwort"],
                        ["Wenn du wach bist", "Klingelt trotzdem", "Klingelt trotzdem", "Leise Frage, ein Tippen"],
                        ["Wenn du weggenickt bist", "Klingelt einmal", "Klingelt, hört dann auf", "Vibration, dann Alarm"],
                        ["Gemacht für", "Aufwachen", "Erinnerungen", "Wach bleiben"],
                    ]},
                ]],
                ["wann", "Wann ein Wach-Check hilft", [
                    {"list": [
                        "**Nachtschicht und Bereitschaft** mit langen ruhigen Strecken.",
                        "**Lernnächte** vor einer Prüfung.",
                        "**Durch die Nacht warten**, etwa auf eine frühe Abfahrt oder einen Anruf.",
                        "**Auf etwas aufpassen** – einen Vorgang, einen Download, ein krankes Haustier.",
                    ]},
                    "In all diesen Fällen ist das Risiko dasselbe: Du merkst selbst nicht, wie du wegdriftest. Ein Wach-Check fragt von außen nach – und wird laut, wenn die Antwort ausbleibt.",
                ]],
                ["ohne-app", "Ohne App", [
                    "Eine einfache Form kannst du selbst bauen: Bitte jemanden, der auch wach ist, dir alle 30 Minuten zu schreiben und anzurufen, wenn du nicht antwortest. Das klappt – solange die andere Person wach bleibt.",
                ]],
                ["was-nicht", "Was ein Wach-Check nicht ist", [
                    "Er misst nicht, wie müde du bist, erkennt keinen Schlaf und ersetzt keine Erholung. Er fragt – die Antwort kommt von dir.",
                ]],
            ],
            "app": {
                "h2": "Stay Awake ist ein Wach-Check",
                "body": [
                    {"steps": [
                        "**0 Sekunden:** Der Bildschirm fragt „Bist du noch wach?“ – auch über dem Sperrbildschirm.",
                        "**10 Sekunden:** Vibration.",
                        "**20 Sekunden:** Alarm mit dem Weckton deines Telefons.",
                    ]},
                    "Bestätige mit dem großen Ja-Knopf oder – wenn du es in den Einstellungen einschaltest – durch Schütteln, Umdrehen oder die Lautstärketaste. Dann beginnt das volle Intervall neu.",
                ],
                "shot": "de-check.webp",
                "alt": "Check: Bist du noch wach?, oder Handy schütteln, großer Ja-Knopf, Sitzung beenden.",
            },
            "faq": [
                ["Erkennt eine Wach-Check-App, wenn ich einschlafe?",
                 ["Nein. Stay Awake nutzt weder Kamera noch Mikrofon und misst nichts an dir. Die App fragt und wird laut, wenn keine Antwort kommt."]],
                ["Was, wenn ich aus Versehen bestätige?",
                 ["Ein einzelner Ruck zählt nicht als Schütteln – es braucht ein bewusstes Schütteln mit mindestens zwei Bewegungen. Die Schüttel-Empfindlichkeit lässt sich in den Einstellungen anpassen."]],
                ["Kann ich bestätigen, bevor die Frage kommt?",
                 ["Ja. In Stay Awake kannst du jederzeit bestätigen; das Intervall beginnt dann ab diesem Moment neu."]],
            ],
        },
        {
            "id": "notringing",
            "slug": "android-wecker-klingelt-nicht",
            "title": "Android-Wecker klingelt nicht? 7 Ursachen und Lösungen",
            "desc": "Wecker bleibt stumm oder kommt zu spät: Wecker-Lautstärke, Nicht stören, Akku-Optimierung, exakte Alarme, Benachrichtigungen, Vollbild. So prüfst du alles.",
            "h1": "Android-Wecker klingelt nicht? 7 Ursachen",
            "teaser": "Lautstärke, Nicht stören, Akkusparen, Berechtigungen – was du prüfen solltest.",
            "answer": "Wenn ein Wecker auf Android stumm bleibt oder zu spät kommt, liegt es meist an einer von sieben Einstellungen: **Wecker-Lautstärke, Nicht stören, Akku-Optimierung, exakte Alarme, Benachrichtigungen, Vollbild-Berechtigung** – oder das Telefon war aus. Prüf sie der Reihe nach und stell dann einen Testwecker in zwei Minuten.",
            "updated": "2026-11-21",
            "updated_label": "21. November 2026",
            "sections": [
                ["ursachen", "7 Ursachen", [
                    {"steps": [
                        "**Wecker-Lautstärke auf null.** Android hat eine eigene Lautstärke für Wecker. Drück eine Lautstärketaste, öffne das Lautstärkefeld und prüf den Regler für Wecker.",
                        "**Nicht stören blockiert Wecker.** Meist sind Wecker im Modus „Nicht stören“ erlaubt, das lässt sich aber abschalten. Sieh unter *Einstellungen → Töne → Nicht stören* nach (die Namen unterscheiden sich je nach Hersteller).",
                        "**Akku-Optimierung stoppt die App.** Manche Hersteller schicken Apps sehr eifrig schlafen. Erlaube in den App-Infos unter *Akku* die uneingeschränkte Nutzung.",
                        "**Keine Berechtigung für exakte Alarme.** Seit Android 12 brauchen andere Apps den Sonderzugriff „Wecker und Erinnerungen“, um pünktlich zu klingeln. Ohne ihn darf Android den Alarm verschieben.",
                        "**Benachrichtigungen aus.** Seit Android 13 müssen Apps um Erlaubnis für Benachrichtigungen fragen; viele Wecker-Apps zeigen ihren Alarm über eine solche an.",
                        "**Vollbild-Berechtigung fehlt.** Ab Android 14 braucht eine App unter Umständen die Erlaubnis, sich im Vollbild über dem Sperrbildschirm zu zeigen.",
                        "**Telefon ausgeschaltet.** Die meisten Android-Telefone klingeln nicht, wenn sie aus sind.",
                    ]},
                ]],
                ["testen", "Richtig testen", [
                    {"steps": [
                        "Stell einen Wecker in zwei Minuten.",
                        "Sperr das Telefon und leg es hin.",
                        "Warte – nicht anfassen.",
                    ]},
                    "Klingelt er, stimmt die Grundeinstellung. Brauchst du den Wecker nachts, teste einmal so, wie du ihn dann nutzt – etwa am Ladekabel.",
                ]],
                ["hersteller", "Telefone mit strengem Akkusparen", [
                    "Manche Hersteller führen eigene Listen, welche Apps im Hintergrund laufen oder automatisch starten dürfen. Kommt ein Wecker immer wieder zu spät, such in den Akku- oder App-Start-Einstellungen einen Eintrag für diese App und erlaube ihr alles.",
                ]],
            ],
            "app": {
                "h2": "Stay Awake prüft das für dich",
                "body": [
                    "Die **Verlässlichkeitsprüfung** in Stay Awake geht diese Punkte durch – Benachrichtigungen, Check- und Alarm-Meldungen, pünktliches Wecken, über dem Sperrbildschirm, Wecker-Lautstärke, Nicht stören, Vibration, Hintergrund und Akku – und zeigt, wie du behebst, was nicht passt.",
                    "Mit **Alarm testen** hörst und spürst du den Alarm fünf Sekunden lang, bevor du dich darauf verlässt.",
                ],
                "shot": "de-reliability.webp",
                "alt": "Verlässlichkeit: Bereit, alle neun Punkte grün.",
            },
            "faq": [
                ["Warum klingelt mein Wecker zu spät?",
                 ["Meist wegen der Akku-Optimierung oder weil die App keine exakten Alarme nutzen darf. Android bündelt den Alarm dann mit anderen Weckvorgängen."]],
                ["Klingelt der Wecker, wenn das Handy lautlos ist?",
                 ["Bei den meisten Android-Telefonen ja, solange die Wecker-Lautstärke nicht auf null steht und „Nicht stören“ Wecker zulässt."]],
                ["Klingelt der Wecker, wenn das Handy aus ist?",
                 ["Bei den meisten Android-Telefonen nicht. Lass das Telefon an und am Ladekabel."]],
            ],
        },
    ],
}
