from decimal import Decimal

from db import db
from models import Internship, Category, Company
from values import Source, Role, WorkModel, CompensationStatus


# Unternehmen abrufen

def unternehmen_abrufen(user_id):

    unternehmen = db.session.execute(
        db.select(Company).filter_by(user_id=user_id)
    ).scalar_one_or_none()

    if unternehmen is None:
        raise PermissionError("Kein Unternehmen vorhanden.")

    if unternehmen.user.role != Role.COMPANY:
        raise PermissionError(
            "Keine Unternehmensberechtigung vorhanden."
        )

    return unternehmen


# Kategorie abrufen

def kategorie_abrufen(slug):

    kategorie = db.session.execute(
        db.select(Category).filter_by(slug=slug)
    ).scalar_one_or_none()

    if kategorie is None:
        raise ValueError(
            "Der Tätigkeitsbereich wurde nicht gefunden."
        )

    return kategorie


# Formulardaten übertragen

def anzeigendaten_uebertragen(anzeige, form):

    kategorie = kategorie_abrufen(form.category_slug.data)

    form.populate_obj(anzeige)

    anzeige.title = anzeige.title.strip()
    anzeige.description = anzeige.description.strip()
    anzeige.requirements = anzeige.requirements.strip()
    anzeige.application_url = anzeige.application_url.strip()

    anzeige.location = "Berlin"

    anzeige.work_model = WorkModel(form.work_model.data)

    anzeige.compensation_status = CompensationStatus(
        form.compensation_status.data
    )

    if anzeige.compensation_status == CompensationStatus.UNPAID:
        anzeige.compensation_amount = Decimal("0.00")

    anzeige.categories = [kategorie]


# Anzeige erstellen

def anzeige_erstellen(form, user_id):

    unternehmen = unternehmen_abrufen(user_id)

    anzeige = Internship(
        company_id=unternehmen.id,
        source=Source.DIRECT,
        external_id=None
    )

    try:

        anzeigendaten_uebertragen(anzeige, form)

        db.session.add(anzeige)
        db.session.commit()

    except Exception:

        db.session.rollback()
        raise

    return anzeige


# Alle eigenen Anzeigen abrufen

def anzeigen_abrufen(user_id):

    unternehmen = unternehmen_abrufen(user_id)

    anzeigen = db.session.execute(
        db.select(Internship)
        .filter_by(
            company_id=unternehmen.id,
            source=Source.DIRECT
        )
        .order_by(Internship.id.desc())
    ).scalars().all()

    return anzeigen


# Einzelne eigene Anzeige abrufen

def anzeige_abrufen(anzeige_id, user_id):

    unternehmen = unternehmen_abrufen(user_id)

    anzeige = db.session.execute(
        db.select(Internship).filter_by(
            id=anzeige_id,
            company_id=unternehmen.id,
            source=Source.DIRECT
        )
    ).scalar_one_or_none()

    return anzeige


# Anzeige bearbeiten

def anzeige_bearbeiten(anzeige_id, form, user_id):

    anzeige = anzeige_abrufen(anzeige_id, user_id)

    if anzeige is None:
        raise LookupError("Anzeige nicht gefunden.")

    try:

        anzeigendaten_uebertragen(anzeige, form)

        db.session.commit()

    except Exception:

        db.session.rollback()
        raise

    return anzeige


# Anzeige löschen

def anzeige_loeschen(anzeige_id, user_id):

    anzeige = anzeige_abrufen(anzeige_id, user_id)

    if anzeige is None:
        raise LookupError("Anzeige nicht gefunden.")

    try:

        db.session.delete(anzeige)
        db.session.commit()

    except Exception:

        db.session.rollback()
        raise

    return True