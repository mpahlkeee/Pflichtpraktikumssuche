
from enum import StrEnum


# Benutzerrollen

class Role(StrEnum):
    STUDENT = "student"
    COMPANY = "company"


# Quellen der Praktikumsanzeigen

class Source(StrEnum):
    DIRECT = "direct"
    JOOBLE = "jooble"
    ADZUNA = "adzuna"
    BA = "ba"


# Arbeitsmodelle

class WorkModel(StrEnum):
    ONSITE = "onsite"
    HYBRID = "hybrid"
    REMOTE = "remote"


# Vergütungsstatus

class CompensationStatus(StrEnum):
    PAID = "paid"
    UNPAID = "unpaid"


# Tätigkeitsbereiche

CATEGORIES = (
    ("marketing", "Marketing"),
    ("vertrieb", "Vertrieb"),
    ("personalwesen", "Personalwesen"),
    ("rechnungswesen", "Rechnungswesen"),
    ("finanzen", "Finanzen"),
    ("controlling", "Controlling"),
    ("unternehmensberatung", "Unternehmensberatung"),
    ("unternehmensentwicklung", "Unternehmensentwicklung"),
    ("strategie", "Strategie"),
    ("projektmanagement", "Projektmanagement"),
    ("produktmanagement", "Produktmanagement"),
    ("einkauf", "Einkauf"),
    ("logistik", "Logistik"),
    ("operations", "Operations"),
    ("datenanalyse", "Datenanalyse"),
    ("digitalisierung", "Digitalisierung"),
    ("kommunikation", "Kommunikation"),
    ("wirtschaftspruefung", "Wirtschaftsprüfung"),
    ("steuern", "Steuern"),
    ("nachhaltigkeit", "Nachhaltigkeit"),
    ("e_commerce", "E-Commerce"),
    ("compliance", "Compliance"),
)


# Tätigkeitsbereiche als Dictionary für weitere Verwendung

TAETIGKEITSBEREICHE = dict(CATEGORIES)


# Suchbegriffe für externe Stellenanzeigen-APIs

API_SUCHBEGRIFFE = {
    "marketing": [
        "Marketing",
        "Social Media",
        "SEO",
        "SEA",
        "Brand Management",
    ],
    "vertrieb": [
        "Sales",
        "Vertrieb",
        "Account Management",
    ],
    "personalwesen": [
        "HR",
        "Human Resources",
        "Recruiting",
        "Personal",
    ],
    "rechnungswesen": [
        "Accounting",
        "Buchhaltung",
        "Rechnungswesen",
    ],
    "finanzen": [
        "Finance",
        "Banking",
        "Investment",
        "Treasury",
    ],
    "controlling": [
        "Controlling",
        "Financial Planning",
        "FP&A",
    ],
    "unternehmensberatung": [
        "Consulting",
        "Unternehmensberatung",
    ],
    "unternehmensentwicklung": [
        "Business Development",
        "Corporate Development",
    ],
    "strategie": [
        "Strategy",
        "Strategie",
    ],
    "projektmanagement": [
        "Project Management",
        "PMO",
        "Projektmanagement",
    ],
    "produktmanagement": [
        "Product Management",
        "Product Owner",
    ],
    "einkauf": [
        "Procurement",
        "Purchasing",
        "Einkauf",
        "Sourcing",
    ],
    "logistik": [
        "Logistics",
        "Supply Chain",
        "Logistik",
    ],
    "operations": [
        "Operations Management",
        "Prozessmanagement",
    ],
    "datenanalyse": [
        "Data Analytics",
        "Business Intelligence",
        "Business Analysis",
    ],
    "digitalisierung": [
        "Digital Transformation",
        "Digitalisierung",
        "IT-Management",
    ],
    "kommunikation": [
        "PR",
        "Public Relations",
        "Corporate Communications",
    ],
    "wirtschaftspruefung": [
        "Audit",
        "Wirtschaftsprüfung",
    ],
    "steuern": [
        "Tax",
        "Steuerberatung",
    ],
    "nachhaltigkeit": [
        "Sustainability",
        "ESG",
        "CSR",
    ],
    "e_commerce": [
        "E-Commerce",
        "Onlinehandel",
        "Marketplace",
    ],
    "compliance": [
        "Compliance",
        "Risk Management",
    ],
}
