
from decimal import Decimal

from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    DateField,
    IntegerField,
    DecimalField,
    PasswordField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired,
    InputRequired,
    NumberRange,
    URL,
    ValidationError,
    Length,
    EqualTo,
    Regexp,
)

from values import CATEGORIES, WorkModel, CompensationStatus


# Formular zum Erstellen und Bearbeiten von Praktikumsanzeigen

class AnzeigeForm(FlaskForm):

    title = StringField(
        "Titel der Praktikumsstelle",
        validators=[
            DataRequired(
                message="Bitte einen Titel eingeben."
            )
        ]
    )

    category_slug = SelectField(
        "Tätigkeitsbereich",
        choices=[("", "Bitte auswählen")] + list(CATEGORIES),
        validators=[
            DataRequired(
                message="Bitte einen Tätigkeitsbereich auswählen."
            )
        ]
    )

    description = TextAreaField(
        "Stellenbeschreibung",
        validators=[
            DataRequired(
                message="Bitte eine Stellenbeschreibung eingeben."
            )
        ]
    )

    requirements = TextAreaField(
        "Anforderungen",
        validators=[
            DataRequired(
                message="Bitte die Anforderungen eingeben."
            )
        ]
    )

    work_model = SelectField(
        "Arbeitsmodell",
        choices=[
            ("", "Bitte auswählen"),
            (WorkModel.ONSITE.value, "Vor Ort"),
            (WorkModel.HYBRID.value, "Hybrid"),
            (WorkModel.REMOTE.value, "Remote"),
        ],
        validators=[
            DataRequired(
                message="Bitte ein Arbeitsmodell auswählen."
            )
        ]
    )

    start_date = DateField(
        "Praktikumsbeginn",
        format="%Y-%m-%d",
        validators=[
            InputRequired(
                message="Bitte ein Startdatum eingeben."
            )
        ]
    )

    duration_months = IntegerField(
        "Praktikumsdauer in Monaten",
        validators=[
            InputRequired(
                message="Bitte eine Praktikumsdauer eingeben."
            ),
            NumberRange(
                min=1,
                message="Die Dauer muss mindestens einen Monat betragen."
            ),
        ]
    )

    compensation_status = SelectField(
        "Vergütungsstatus",
        choices=[
            ("", "Bitte auswählen"),
            (CompensationStatus.PAID.value, "Bezahlt"),
            (CompensationStatus.UNPAID.value, "Unbezahlt"),
        ],
        validators=[
            DataRequired(
                message="Bitte einen Vergütungsstatus auswählen."
            )
        ]
    )

    compensation_amount = DecimalField(
        "Monatliche Vergütung in Euro",
        places=2
    )

    application_url = StringField(
        "Bewerbungslink",
        validators=[
            DataRequired(
                message="Bitte einen Bewerbungslink eingeben."
            ),
            URL(
                message="Bitte eine gültige URL eingeben."
            ),
        ]
    )

    submit = SubmitField("Speichern")


    # Abhängige Validierung der Vergütung

    def validate_compensation_amount(self, field):

        if self.compensation_status.data == CompensationStatus.UNPAID.value:

            field.errors.clear()
            field.data = None
            return

        if self.compensation_status.data == CompensationStatus.PAID.value:

            if field.data is None:

                raise ValidationError(
                    "Bitte eine monatliche Vergütung eingeben."
                )

            if (
                not field.data.is_finite()
                or field.data <= 0
                or field.data > Decimal("99999999.99")
                or field.data.as_tuple().exponent < -2
            ):

                raise ValidationError(
                    "Bitte einen gültigen positiven Betrag "
                    "mit maximal zwei Nachkommastellen eingeben."
                )


    # Bewerbungslink auf HTTP und HTTPS beschränken

    def validate_application_url(self, field):

        if not field.data.startswith(("https://", "http://")):

            raise ValidationError(
                "Der Link muss mit http:// oder https:// beginnen."
            )


# Formular zum Löschen einer Praktikumsanzeige

class AnzeigeLoeschenForm(FlaskForm):

    submit = SubmitField("Löschen")


# Loginformular

class LoginForm(FlaskForm):

    email = StringField(
        "E-Mail",
        validators=[
            DataRequired(message="Bitte eine E-Mail-Adresse eingeben."),
            Regexp(
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
                message="Bitte eine gültige E-Mail-Adresse eingeben."
            ),
        ]
    )

    password = PasswordField(
        "Passwort",
        validators=[DataRequired(message="Bitte ein Passwort eingeben.")]
    )

    submit = SubmitField("Anmelden")


# Registrierungsformular

class RegistrierungForm(FlaskForm):

    email = StringField(
        "E-Mail",
        validators=[
            DataRequired(
                message="Bitte eine E-Mail-Adresse eingeben."
            ),
            Regexp(
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
                message="Bitte eine gültige E-Mail-Adresse eingeben."
            ),
        ]
    )

    role = SelectField(
        "Ich registriere mich als",
        choices=[
            ("student", "Studierende/r"),
            ("company", "Unternehmen"),
        ],
        validators=[
            DataRequired(
                message="Bitte eine Rolle auswählen."
            )
        ]
    )

    company_name = StringField(
        "Unternehmensname"
    )

    password = PasswordField(
        "Passwort",
        validators=[
            DataRequired(
                message="Bitte ein Passwort eingeben."
            ),
            Length(
                min=8,
                message="Das Passwort muss mindestens 8 Zeichen lang sein."
            ),
        ]
    )

    confirm_password = PasswordField(
        "Passwort wiederholen",
        validators=[
            DataRequired(
                message="Bitte das Passwort wiederholen."
            ),
            EqualTo(
                "password",
                message="Die Passwörter stimmen nicht überein."
            ),
        ]
    )

    submit = SubmitField("Registrieren")


    # Unternehmensname nur bei Unternehmen erforderlich

    def validate_company_name(self, field):

        if self.role.data == "company" and not (field.data or "").strip():

            raise ValidationError(
                "Bitte einen Unternehmensnamen eingeben."
            )
