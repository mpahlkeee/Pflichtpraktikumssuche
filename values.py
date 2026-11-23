from enum import StrEnum


class Role(StrEnum):
    STUDENT = "student"
    COMPANY = "company"


class Source(StrEnum):
    DIRECT = "direct"
    JOOBLE = "jooble"
    ADZUNA = "adzuna"
    BA = "ba"


class WorkModel(StrEnum):
    ONSITE = "onsite"
    HYBRID = "hybrid"
    REMOTE = "remote"


class CompensationStatus(StrEnum):
    PAID = "paid"
    UNPAID = "unpaid"


CATEGORIES = (
    ("marketing", "Marketing"),
    ("personalwesen", "Personalwesen"),
    ("controlling", "Controlling"),
    ("finanz-rechnungswesen", "Finanz- und Rechnungswesen"),
    ("vertrieb-kundenmanagement", "Vertrieb und Kundenmanagement"),
    ("business-development", "Business Development"),
    ("einkauf-supply-chain", "Einkauf und Supply Chain Management"),
    ("projektmanagement", "Projektmanagement"),
    ("unternehmensberatung", "Unternehmensberatung"),
)
