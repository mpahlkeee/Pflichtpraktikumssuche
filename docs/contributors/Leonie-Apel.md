[← Contributors](README.md)

# Leonie Apel

## Meta-Goals

### Target grade

Ich strebe die Note 1,3 an. Ich erwarte keine 1,0, da ich zu ersten Mal die Programme, sowie Python nutze. Ich bin aber zuversichtlich, dass wir uns gut einarbeiten können.

### Personal goals

Ich möchte die Grundlagen der Full-Stack-Webentwicklung kennenlernen und verstehen, wie Frontend, Backend und Datenbanken zusammenarbeiten. Dabei möchte ich praktische Erfahrungen in der Entwicklung von Webanwendungen sammeln und nachvollziehen, wie diese aufgebaut sind und funktionieren.

Ein besonderer Schwerpunkt liegt für mich auf dem Umgang mit Git und Github. Ich möchte lernen, Versionskontrolle sicher anzuwenden, Änderungen nachzuverfolgen, Branches zu erstellen und mit anderen Personen gemeinsam an Projekten zu arbeiten. Mein Ziel ist es, Git und GitHub auch in zukünftigen Projekten selbstständig und sicher einsetzen zu können.

Auch wenn ich später  nicht direkt in der Full-Stack-Entwicklung arbeiten möchte, halte ich es für wichtig, die grundlegenden Prinzipien der Webentwicklung zu verstehen. Dadurch möchte ich mein technisches Verständnis erweitern, meine Programmierkenntnisse vertiefen und besser nachvollziehen können, wie Softwareprojekte strukturiert und umgesetzt werden.


---

## Eidesstattliche Erklärung

**[Leonie Apel, Matrikelnr.: 77207691939]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

KI-Systeme (z.B. LLM-basierte Werkzeuge) habe ich ausschließlich als Hilfsmittel gemäß der Vorgaben im Modul eingesetzt. Insbesondere habe ich zu keiner Zeit und in keiner Weise agentische Systeme ("Agentic AI") genutzt. Jegliche Nutzung habe ich vollständig und gemäß der geltenden Regeln und Vorgaben an HWR Berlin und Fachbereich 1 dokumentiert. 

Mir ist bewusst, dass folgendes als Täuschungsversuch gewertet wird und zu einer Beurteilung der Modulleistung mit "nicht ausreichend" führt:

- Die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe;
- Die nicht vollständige Offenlegung genutzter KI-Systeme;
- Jegliche Nutzung von Agentic AI.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Vertical Feature Ownership

### Erstellung und Verwaltung von Praktikumsanzeigen

Unternehmen können eigenständig Pflichtpraktikumsanzeigen auf unserer Plattform erstellen, bearbeiten und löschen. Dadurch wird das Angebot der über die API eingebundenen Stellenanzeigen ergänzt.

Das Feature umfasst die Implementierung der Backend-Logik, die Datenbankanbindung, die Erstellung der Benutzeroberflächen, die Validierung der Eingaben sowie die Überprüfung der Zugriffsberechtigungen.

Zusätzlich wurden einheitliche BWL-spezifische Tätigkeitsbereiche definiert und zentral hinterlegt, um eine konsistente Kategorisierung der Praktikumsanzeigen zu ermöglichen.

### Step-by-Step Walkthrough

1. Als Unternehmen anmelden.
2. Über die Navigation „Meine Anzeigen“ aufrufen.
3. Eine neue Praktikumsanzeige erstellen.
4. Die erforderlichen Angaben ausfüllen.
5. Einen vordefinierten Tätigkeitsbereich auswählen.
6. Die Praktikumsanzeige speichern.
7. Die erstellte Anzeige unter „Meine Anzeigen“ aufrufen.
8. Eine bestehende Anzeige bearbeiten und die Änderungen speichern.
9. Eine bestehende Anzeige löschen.

Unternehmen können ausschließlich ihre eigenen Praktikumsanzeigen bearbeiten und löschen. Der Standort ist auf Berlin beschränkt.


| Activities | Proof, e.g., git commits | Sources used |
|---|---|---|
| Implementierung der Erstellung, Bearbeitung und Löschung von Praktikumsanzeigen (CRUD) | [a7a6f36](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/a7a6f36) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/) |
| Datenbankanbindung und Speicherung der Praktikumsanzeigen | [a7a6f36](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/a7a6f36) | [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/stable/) |
| Erstellung der Benutzeroberflächen zur Anzeigenverwaltung | [a7a6f36](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/a7a6f36) | [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/) |
| Implementierung der Eingabevalidierung und Zugriffsberechtigungen | [a7a6f36](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/a7a6f36) | - |
| Definition und Zentralisierung BWL-spezifischer Tätigkeitsbereiche | [a7a6f36](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/a7a6f36) | ChatGPT (siehe AI Directory) |
| Anpassung der `.gitignore` | [a7a6f36](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/a7a6f36) | - |
| Dokumentation der KI-Nutzung im AI Directory | [c7ddc59](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/c7ddc59) | - |
| Integration des Features in den Main-Branch | [3fa2dd8](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3fa2dd8), [Pull Request #3](https://github.com/mpahlkeee/Pflichtpraktikumssuche/pull/3) | – |

---

## Portfolio Ownership

Ich mache Portfolio **D** in unserem **4-Personen** Team.

**In addition**, supply ample proof of ownership, primarily through work diary entries, git commit traces, and other useful artifacts. Maintain a table like this.]

| Portfolio Task | Proof |
| :-- | :-- |
| **Discovery Process** | |
| Plan discovery activities | [Discovery Plan](../product-discovery/material/02-up/.todo) |
| Maintain discovery evidence | *01.11.:* I reminded everybody to upload their discovery evidence |
| | *05.11.:* I checked all uploads for completeness |
**API** | |
| Integrate API behavior | [74a6b7](https://github.com/hwrberlin/fswd/commit/74a6b7) |
| | |
| | |

---

## Design Decisions that I led

- [03: Eigene Stellenanzeigen für Unternehmen](dd-03.md)

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| --- | --- | --- | --- | --- |
| 01 | ChatGPT | Identifikation, Strukturierung und Kategorisierung relevanter Tätigkeitsbereiche für BWL-Pflichtpraktika | `values.py`, Tätigkeitskategorien, Filterkriterien und API-Suchbegriffe | ChatGPT wurde zur Sammlung und Systematisierung relevanter betriebswirtschaftlicher Tätigkeitsbereiche eingesetzt. Zusätzlich wurden passende Suchbegriffe und Synonyme für die Zuordnung externer Praktikumsanzeigen vorgeschlagen. Die Ergebnisse dienten als Grundlage für die Definition einheitlicher Tätigkeitskategorien und Filtermöglichkeiten. Prompt: „Welche Tätigkeitsbereiche gibt es für BWL-Praktika? Erstelle mir eine Liste mit relevanten Begriffen.“ |
| 02 | ChatGPT | Statische Codeüberprüfung und Identifikation möglicher Fehler und veralteter Codebestandteile | `app.py`, `db.py`, `models.py`, `anzeigen.py`, `forms.py`, HTML-Templates, `requirements.txt` | Unterstützung bei der Überprüfung der bisherigen Implementierung auf Inkonsistenzen zwischen Datenbankmodellen, Formularen, Flask-Routen und Templates. Bereitstellung von Terminalbefehlen zur Identifikation veralteter Datenbankabfragen, Formularfeldnamen und JavaScript-Implementierungen. Identifikation eines fehlerhaften Template-Dateinamens anhand der Git-Ausgabe. Es wurden keine automatisierten Funktionstests durchgeführt. |
| 03 | ChatGPT | Unterstützung bei der Versionsverwaltung mit Git und Optimierung der Projektkonfiguration | `.gitignore`, Git-Repository, Branch `feature/anzeigenverwaltung` | Unterstützung bei der Interpretation von Terminalausgaben und der Überprüfung geänderter, gelöschter und neu erstellter Dateien. Generierung einer erweiterten `.gitignore` zum Ausschluss von Python-Cache-Dateien, virtuellen Umgebungen und sensiblen Konfigurationsdateien. Beratung zum Umgang mit lokalen Änderungen an der gemeinsam verwalteten SQLite-Datenbank und zur Vorbereitung des Commits. Die Terminalbefehle wurden eigenständig ausgeführt. |

