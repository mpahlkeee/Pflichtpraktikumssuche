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

[First, briefly describe the vertical feature(s) that you owned.

Next, provide a **step-by-step walkthrough** of owned vertical feature(s) that examiner can follow in app. Ensure this matches actually implemented functionality.

**In addition**, supply ample proof of ownership, primarily through exemplary git commit traces. For every vertical feature you owned, maintain a table like this.]

| Activities | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| [Design Challenge research] | [Research traces](../product-discovery/01-design-challenge.md#raw-materia) | See left |
| [Refactor to use Flask Blueprints] | [d816e4](https://github.com/hwrberlin/fswd/commit/d816e4), [75a6c1](https://github.com/hwrberlin/fswd/commit/75a6c1) | [Flask Documentation](https://flask.palletsprojects.com/en/stable/blueprints/#the-concept-of-blueprints) |
|  |  |  |
|  |  |  |
|  |  |  |

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

- [00: Title](../design-decisions/dd-00.md)
- [01: How to access the database - SQL or SQLAlchemy](../design-decisions/dd-01.md)

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| --- | --- | --- | --- | --- |
| 01 | ChatGPT | Identifikation, Strukturierung und Kategorisierung relevanter Tätigkeitsbereiche für BWL-Pflichtpraktika | `values.py`, Tätigkeitskategorien, Filterkriterien und API-Suchbegriffe | ChatGPT wurde zur Sammlung und Systematisierung relevanter betriebswirtschaftlicher Tätigkeitsbereiche eingesetzt. Zusätzlich wurden passende Suchbegriffe und Synonyme für die Zuordnung externer Praktikumsanzeigen vorgeschlagen. Die Ergebnisse dienten als Grundlage für die Definition einheitlicher Tätigkeitskategorien und Filtermöglichkeiten. Prompt: „Welche Tätigkeitsbereiche gibt es für BWL-Praktika? Erstelle mir eine Liste mit relevanten Begriffen.“ |
| 02 | ChatGPT | Statische Codeüberprüfung und Identifikation möglicher Fehler und veralteter Codebestandteile | `app.py`, `db.py`, `models.py`, `anzeigen.py`, `forms.py`, HTML-Templates, `requirements.txt` | Unterstützung bei der Überprüfung der bisherigen Implementierung auf Inkonsistenzen zwischen Datenbankmodellen, Formularen, Flask-Routen und Templates. Bereitstellung von Terminalbefehlen zur Identifikation veralteter Datenbankabfragen, Formularfeldnamen und JavaScript-Implementierungen. Identifikation eines fehlerhaften Template-Dateinamens anhand der Git-Ausgabe. Es wurden keine automatisierten Funktionstests durchgeführt. |
| 03 | ChatGPT | Unterstützung bei der Versionsverwaltung mit Git und Optimierung der Projektkonfiguration | `.gitignore`, Git-Repository, Branch `feature/anzeigenverwaltung` | Unterstützung bei der Interpretation von Terminalausgaben und der Überprüfung geänderter, gelöschter und neu erstellter Dateien. Generierung einer erweiterten `.gitignore` zum Ausschluss von Python-Cache-Dateien, virtuellen Umgebungen und sensiblen Konfigurationsdateien. Beratung zum Umgang mit lokalen Änderungen an der gemeinsam verwalteten SQLite-Datenbank und zur Vorbereitung des Commits. Die Terminalbefehle wurden eigenständig ausgeführt. |

