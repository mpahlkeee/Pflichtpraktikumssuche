[← Contributors](README.md)

# Lea Karadas

## Meta-Goals

### Target grade
Ich strebe die Note 1,3 an, da ich damit sehr zufrieden wäre und weiß, dass der Kurs anspruchsvoll ist, da wir zum ersten mal Python benutzen.

### Personal goals
Meine persönlichen Ziele für dieses Modul sind, meine Programmierkenntnisse zu verbessern und zu lernen wie man vollständige Webanwendungen entwickelt. Ich möchte sowohl die Frontend- als auch die Backend-Entwicklung besser verstehen und praktische Erfahrungen mit Datenbanken und APIs sammeln. 

Ein weiteres Ziel ist es, Git und GitHub sicher zu nutzen, um meinen Code zu verwalten, Änderungen nachzuverfolgen und die Zusammenarbeit im Team zu erleichtern.

Außerdem möchte ich meine Problemlösungsfähigkeiten verbessern und lernen, effektiv im Team zusammenzuarbeiten.

## Eidesstattliche Erklärung

**[Lea Karadas, Matrikelnr.: 77202285794]**

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

### Registrierung und Login

Ich war für die Implementierung der Registrierung und des Login-Systems von Praktify verantwortlich. Dazu gehörten die Registrierung von Studierenden und Unternehmen, die Anmeldung und Abmeldung, die sichere Speicherung von Passwörtern, die Sessionverwaltung sowie die Verwaltung der Benutzerrollen und Zugriffsrechte.

Nutzer können sich mit ihrer E-Mail-Adresse und ihrem Passwort registrieren und dabei ihre Rolle (Studierende oder Unternehmen) auswählen. Nach erfolgreicher Registrierung werden sie automatisch angemeldet und zur Startseite weitergeleitet. Bereits registrierte Nutzer können sich mit ihren Zugangsdaten anmelden und bleiben während der Nutzung der Anwendung eingeloggt. Außerdem können sie sich wieder abmelden. Passwörter werden mithilfe eines Hash-Verfahrens sicher gespeichert. Bestimmte Funktionen sind abhängig von der jeweiligen Benutzerrolle zugänglich.

### Schritt-für-Schritt-Durchführung in der App

1. Praktify öffnen.
2. Zur Registrierungsseite navigieren.
3. Als Studierende oder Unternehmen registrieren.
4. Nach erfolgreicher Registrierung wird man automatisch angemeldet und zur Startseite weitergeleitet.
5. Mit einem bestehenden Account über die Login-Seite anmelden.
6. Prüfen, ob man während der Navigation durch die Anwendung angemeldet bleibt.
7. Über die Logout-Funktion abmelden.


## Nachweis der Eigenleistung

| Aktivitäten | Nachweis, z. B. Git-Commits | Verwendete Quellen |
| --- | --- | --- |
| Registrierung von Studierenden | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials und Flask-Dokumentation |
| Registrierung von Unternehmen | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials und Flask-Dokumentation |
| Login und Authentifizierung | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials und Flask-Dokumentation |
| Sichere Passwortspeicherung | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials |
| Sessionverwaltung | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials und Flask-Dokumentation |
| Logout-Funktion | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials und Flask-Dokumentation |
| Benutzerrollen und Zugriffsrechte | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials |
| Login- und Registrierungsoberfläche | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Projekt-Tutorials und HTML-Dokumentation | | [Commit 3b49796](https://github.com/mpahlkeee/Pflichtpraktikumssuche/commit/3b49796) | Flask-Dokumentation |

---

## Design Decisions that I led

- [00: Title](../design-decisions/dd-00.md)
- [01: How to access the database - SQL or SQLAlchemy](../design-decisions/dd-01.md)

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
|---|---|---|---|---|
| 01 | ChatGPT | Unterstützung beim Verständnis der Funktionsweise von Flask-Routen und der Umsetzung von Login und Registrierung | `app.py`, `forms.py` | ChatGPT wurde verwendet, um die Funktionsweise von Flask-Routen, GET- und POST-Anfragen sowie die Formularverarbeitung zu erklären. Der Code wurde selbstständig geschrieben und mithilfe der Erklärungen umgesetzt. Prompt: „Kannst du mir erklären, wie eine Login- und Registrierungsfunktion in Flask aufgebaut ist und welche Schritte bei einer Anmeldung durchgeführt werden?“ |
| 02 | ChatGPT | Unterstützung bei der Fehlersuche im Login- und Registrierungsprozess | `app.py`, `login.html`, `register.html` | Bei auftretenden Problemen wurden Fehlverhalten und Fehlermeldungen beschrieben, um mögliche Ursachen zu verstehen und Lösungsansätze zu erhalten. Die vorgeschlagenen Lösungen wurden selbst überprüft und umgesetzt. Prompt: „Nach der Registrierung werde ich direkt wieder zur Login-Seite weitergeleitet. Ich möchte stattdessen, dass der Nutzer automatisch angemeldet wird und auf die Startseite gelangt. Woran könnte das liegen?“ |
| 03 | ChatGPT | Unterstützung beim Verständnis der Benutzerrollen und rollenabhängigen Zugriffsrechte | `app.py`, `base.html` | ChatGPT wurde zur Erklärung der Unterscheidung zwischen Studierenden und Unternehmen sowie der rollenabhängigen Darstellung von Navigationselementen und Funktionen verwendet. Die Umsetzung erfolgte selbstständig. Prompt: „Wie kann ich in Flask zwischen Studierenden und Unternehmen unterscheiden und dafür sorgen, dass bestimmte Navigationselemente oder Funktionen nur für die jeweilige Benutzerrolle angezeigt werden?“ |
| 04 | ChatGPT | Unterstützung bei der Formulierung und Strukturierung der Projektdokumentation | `docs/design-decisions/README.md`, AI Directory | ChatGPT wurde zur sprachlichen Überarbeitung und Strukturierung der Beschreibung der eigenen Implementierung sowie zur Unterstützung bei der Dokumentation der Eigenleistung verwendet. Prompt: „Kannst du die Beschreibung meiner Implementierung von Login und Registrierung verständlicher und strukturierter formulieren, ohne die technischen Inhalte zu verändern?“ |
