
import os
from pathlib import Path

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    session,
    abort,
    flash,
    request
)

from flask_bootstrap import Bootstrap5

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from db import db
from models import Category, User, Company
from values import CATEGORIES
from forms import (
    AnzeigeForm,
    AnzeigeLoeschenForm,
    LoginForm,
    RegistrierungForm
)

from anzeigen import (
    unternehmen_abrufen,
    anzeigen_abrufen,
    anzeige_abrufen,
    anzeige_erstellen,
    anzeige_bearbeiten,
    anzeige_loeschen
)


# Flask-Initialisierung

app = Flask(__name__)

app.config["SECRET_KEY"] = (
    os.environ.get("SECRET_KEY")
    or "dev-secret-key-change-me"
)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{Path(app.root_path) / 'database.db'}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Datenbank und Bootstrap initialisieren

db.init_app(app)

bootstrap = Bootstrap5(app)


# Datenbanktabellen und Tätigkeitsbereiche anlegen

with app.app_context():

    db.create_all()

    for slug, name in CATEGORIES:

        kategorie = db.session.execute(
            db.select(Category).filter_by(slug=slug)
        ).scalar_one_or_none()

        if kategorie is None:

            kategorie = Category(
                slug=slug,
                name=name
            )

            db.session.add(kategorie)

    db.session.commit()


# Allgemeine Seiten

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/praktika")
def praktika():

    return render_template("praktika.html")


@app.route("/favoriten")
def favoriten():

    return render_template("favoriten.html")


# Login

@app.route("/login", methods=["GET", "POST"])
def login():

    # Wenn der Nutzer bereits angemeldet ist,
    # direkt zur Startseite weiterleiten
    if session.get("user_id"):

        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data.strip().lower()

        password = form.password.data

        # Nutzer anhand der E-Mail suchen
        user = User.query.filter_by(email=email).first()

        # Login überprüfen
        if user and check_password_hash(
            user.password_hash,
            password
        ):

            # Alte Session löschen
            session.clear()

            # Nutzer anmelden
            session["user_id"] = user.id
            session["role"] = user.role.value

            flash(
                "Du bist erfolgreich angemeldet!",
                "success"
            )

            # Zur Startseite weiterleiten
            return redirect(url_for("index"))

        else:

            flash(
                "E-Mail oder Passwort ist falsch.",
                "danger"
            )

    elif request.method == "POST":

        flash("Bitte prüfe deine Eingaben.", "danger")

    return render_template("login.html", form=form)


# Registrierung

@app.route("/register", methods=["GET", "POST"])
def register():

    # Wenn der Nutzer bereits angemeldet ist,
    # direkt zur Startseite weiterleiten
    if session.get("user_id"):

        return redirect(url_for("index"))

    form = RegistrierungForm()

    if form.validate_on_submit():

        email = form.email.data.strip().lower()

        # Prüfen, ob die E-Mail bereits existiert
        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                "Diese E-Mail-Adresse ist bereits registriert.",
                "danger"
            )

            return render_template(
                "register.html",
                form=form
            )

        # Passwort verschlüsseln
        password_hash = generate_password_hash(
            form.password.data
        )

        # Nutzer erstellen
        user = User(
            email=email,
            password_hash=password_hash,
            role=form.role.data
        )

        db.session.add(user)

        db.session.flush()

        # Falls sich ein Unternehmen registriert
        if form.role.data == "company":

            company = Company(
                user_id=user.id,
                name=form.company_name.data
            )

            db.session.add(company)

        # Daten speichern
        db.session.commit()

        # Alte Session löschen
        session.clear()

        # Nutzer direkt anmelden
        session["user_id"] = user.id
        session["role"] = user.role.value

        flash(
            "Registrierung erfolgreich! Du bist jetzt angemeldet.",
            "success"
        )

        # Zur Startseite weiterleiten
        return redirect(url_for("index"))

    return render_template(
        "register.html",
        form=form
    )


# Praktikumsanzeigen verwalten

@app.route("/unternehmen/anzeigen")
def anzeigen_verwalten():

    user_id = session.get("user_id")

    if user_id is None:

        return redirect(url_for("login"))

    try:

        anzeigen = anzeigen_abrufen(user_id)

    except PermissionError:

        abort(403)

    return render_template(
        "anzeigen_verwalten.html",
        anzeigen=anzeigen
    )


# Praktikumsanzeige erstellen

@app.route(
    "/unternehmen/anzeigen/erstellen",
    methods=["GET", "POST"]
)
def erstellen():

    user_id = session.get("user_id")

    if user_id is None:

        return redirect(url_for("login"))

    try:

        unternehmen_abrufen(user_id)

        form = AnzeigeForm()

        if request.method == "POST" and form.validate():

            anzeige_erstellen(
                form,
                user_id
            )

            flash(
                "Die Praktikumsanzeige wurde erstellt.",
                "success"
            )

            return redirect(
                url_for("anzeigen_verwalten")
            )

    except PermissionError:

        abort(403)

    return render_template(
        "anzeige_erstellen.html",
        form=form
    )


# Praktikumsanzeige bearbeiten

@app.route(
    "/unternehmen/anzeigen/<int:anzeige_id>/bearbeiten",
    methods=["GET", "POST"]
)
def bearbeiten(anzeige_id):

    user_id = session.get("user_id")

    if user_id is None:

        return redirect(url_for("login"))

    try:

        anzeige = anzeige_abrufen(
            anzeige_id,
            user_id
        )

        if anzeige is None:

            abort(404)

        if request.method == "POST":

            form = AnzeigeForm()

            if form.validate():

                anzeige_bearbeiten(
                    anzeige_id,
                    form,
                    user_id
                )

                flash(
                    "Die Änderungen wurden gespeichert.",
                    "success"
                )

                return redirect(
                    url_for("anzeigen_verwalten")
                )

        else:

            form = AnzeigeForm(obj=anzeige)

            if anzeige.categories:

                form.category_slug.data = (
                    anzeige.categories[0].slug
                )

    except PermissionError:

        abort(403)

    except LookupError:

        abort(404)

    return render_template(
        "anzeige_bearbeiten.html",
        form=form,
        anzeige=anzeige
    )


# Löschen einer Praktikumsanzeige bestätigen

@app.route(
    "/unternehmen/anzeigen/<int:anzeige_id>/loeschen-bestaetigen"
)
def loeschen_bestaetigen(anzeige_id):

    user_id = session.get("user_id")

    if user_id is None:

        return redirect(url_for("login"))

    try:

        anzeige = anzeige_abrufen(
            anzeige_id,
            user_id
        )

        if anzeige is None:

            abort(404)

    except PermissionError:

        abort(403)

    form = AnzeigeLoeschenForm()

    return render_template(
        "anzeige_loeschen.html",
        anzeige=anzeige,
        form=form
    )


# Praktikumsanzeige löschen

@app.route(
    "/unternehmen/anzeigen/<int:anzeige_id>/loeschen",
    methods=["POST"]
)
def loeschen(anzeige_id):

    user_id = session.get("user_id")

    if user_id is None:

        return redirect(url_for("login"))

    form = AnzeigeLoeschenForm()

    if not form.validate():

        abort(400)

    try:

        anzeige_loeschen(
            anzeige_id,
            user_id
        )

    except PermissionError:

        abort(403)

    except LookupError:

        abort(404)

    flash(
        "Die Praktikumsanzeige wurde gelöscht.",
        "success"
    )

    return redirect(
        url_for("anzeigen_verwalten")
    )


# Logout

@app.route("/logout")
def logout():

    # Session löschen
    session.clear()

    flash(
        "Du wurdest erfolgreich abgemeldet.",
        "success"
    )

    return redirect(url_for("index"))


# Anwendung starten

if __name__ == "__main__":

    app.run(debug=True)
