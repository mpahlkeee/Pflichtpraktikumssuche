from db import db
from values import CompensationStatus, Role, Source, WorkModel


def enum_column(enum_class, constraint_name):
    return db.Enum(
        enum_class,
        name=constraint_name,
        native_enum=False,
        create_constraint=True,
        validate_strings=True,
        values_callable=lambda members: [member.value for member in members],
    )


# Benutzer

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(
        db.Text(collation="NOCASE"),
        unique=True,
        nullable=False,
    )

    password_hash = db.Column(db.Text, nullable=False)

    role = db.Column(
        enum_column(Role, "ck_users_role"),
        nullable=False,
    )

    company = db.relationship(
        "Company",
        back_populates="user",
        passive_deletes="all",
        uselist=False,
    )

    favorites = db.relationship(
        "Favorite",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


# Unternehmen

class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="RESTRICT"),
        unique=True,
        nullable=False,
    )

    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    website_url = db.Column(db.Text)

    user = db.relationship(
        "User",
        back_populates="company",
    )

    internships = db.relationship(
        "Internship",
        back_populates="company",
        passive_deletes="all",
    )


# Praktikumsanzeigen

class Internship(db.Model):
    __tablename__ = "internships"

    __table_args__ = (
        db.UniqueConstraint(
            "source",
            "external_id",
            name="uq_internships_source_external_id",
        ),

        db.CheckConstraint(
            f"(source = '{Source.DIRECT.value}' "
            "AND company_id IS NOT NULL "
            "AND external_id IS NULL) "
            f"OR (source <> '{Source.DIRECT.value}' "
            "AND external_id IS NOT NULL "
            "AND length(trim(external_id)) > 0)",
            name="ck_internships_source_identity",
        ),

        db.CheckConstraint(
            "duration_min_weeks IS NULL OR duration_min_weeks > 0",
            name="ck_internships_duration_min",
        ),

        db.CheckConstraint(
            "duration_max_weeks IS NULL OR duration_max_weeks > 0",
            name="ck_internships_duration_max",
        ),

        db.CheckConstraint(
            "duration_min_weeks IS NULL OR duration_max_weeks IS NULL "
            "OR duration_min_weeks <= duration_max_weeks",
            name="ck_internships_duration_order",
        ),

        db.CheckConstraint(
            "location = 'Berlin'",
            name="ck_internships_location",
        ),

        db.CheckConstraint(
            "duration_months IS NULL OR duration_months > 0",
            name="ck_internships_duration_months",
        ),

        db.CheckConstraint(
            "compensation_amount IS NULL OR compensation_amount >= 0",
            name="ck_internships_compensation_amount",
        ),

        db.CheckConstraint(
            "compensation_status != 'unpaid' "
            "OR compensation_amount IS NULL "
            "OR compensation_amount = 0",
            name="ck_internships_unpaid_amount",
        ),

        db.CheckConstraint(
            "compensation_status != 'paid' "
            "OR compensation_amount IS NULL "
            "OR compensation_amount > 0",
            name="ck_internships_paid_amount",
        ),

        db.Index("ix_internships_company_id", "company_id"),
    )

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id", ondelete="RESTRICT"),
    )

    source = db.Column(
        enum_column(Source, "ck_internships_source"),
        nullable=False,
    )

    external_id = db.Column(db.Text)

    title = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=False)

    requirements = db.Column(db.Text)

    location = db.Column(
        db.Text,
        nullable=False,
        default="Berlin",
        server_default="Berlin",
    )

    work_model = db.Column(
        enum_column(WorkModel, "ck_internships_work_model")
    )

    duration_min_weeks = db.Column(db.Integer)
    duration_max_weeks = db.Column(db.Integer)
    duration_months = db.Column(db.Integer)

    compensation_status = db.Column(
        enum_column(
            CompensationStatus,
            "ck_internships_compensation_status",
        )
    )

    compensation_amount = db.Column(db.Numeric(10, 2))

    start_date = db.Column(db.Date)

    application_url = db.Column(db.Text)

    company = db.relationship(
        "Company",
        back_populates="internships",
    )

    categories = db.relationship(
        "Category",
        secondary="internship_categories",
        back_populates="internships",
        passive_deletes=True,
    )

    favorites = db.relationship(
        "Favorite",
        back_populates="internship",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


# Tätigkeitsbereiche

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)

    internships = db.relationship(
        "Internship",
        secondary="internship_categories",
        back_populates="categories",
        passive_deletes=True,
    )


# Zuordnung von Praktikumsanzeigen zu Tätigkeitsbereichen

class InternshipCategory(db.Model):
    __tablename__ = "internship_categories"

    __table_args__ = (
        db.Index("ix_internship_categories_category_id", "category_id"),
    )

    internship_id = db.Column(
        db.Integer,
        db.ForeignKey("internships.id", ondelete="CASCADE"),
        primary_key=True,
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id", ondelete="CASCADE"),
        primary_key=True,
    )


# Favoriten

class Favorite(db.Model):
    __tablename__ = "favorites"

    __table_args__ = (
        db.Index("ix_favorites_internship_id", "internship_id"),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )

    internship_id = db.Column(
        db.Integer,
        db.ForeignKey("internships.id", ondelete="CASCADE"),
        primary_key=True,
    )

    user = db.relationship(
        "User",
        back_populates="favorites",
    )

    internship = db.relationship(
        "Internship",
        back_populates="favorites",
    )