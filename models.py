from datetime import date

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date,
    CheckConstraint,
    Enum,
    ForeignKey,
    Index,
    UniqueConstraint,
)
from sqlalchemy.orm import declarative_base, relationship

from values import CompensationStatus, Role, Source, WorkModel


Base = declarative_base()


def enum_column(enum_class, constraint_name):
    return Enum(
        enum_class,
        name=constraint_name,
        native_enum=False,
        create_constraint=True,
        validate_strings=True,
        values_callable=lambda members: [member.value for member in members],
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(Text(collation="NOCASE"), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(enum_column(Role, "ck_users_role"), nullable=False)

    company = relationship(
        "Company",
        back_populates="user",
        passive_deletes="all",
        uselist=False,
    )

    favorites = relationship(
        "Favorite",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="RESTRICT"),
        unique=True,
        nullable=False,
    )
    name = Column(Text, nullable=False)
    description = Column(Text)
    website_url = Column(Text)

    user = relationship(
        "User",
        back_populates="company",
    )

    internships = relationship(
        "Internship",
        back_populates="company",
        passive_deletes="all",
    )


class Internship(Base):
    __tablename__ = "internships"

    __table_args__ = (
        UniqueConstraint(
            "source",
            "external_id",
            name="uq_internships_source_external_id",
        ),
        CheckConstraint(
            f"(source = '{Source.DIRECT.value}' "
            "AND company_id IS NOT NULL "
            "AND external_id IS NULL) "
            f"OR (source <> '{Source.DIRECT.value}' "
            "AND external_id IS NOT NULL "
            "AND length(trim(external_id)) > 0)",
            name="ck_internships_source_identity",
        ),
        CheckConstraint(
            "duration_min_weeks IS NULL OR duration_min_weeks > 0",
            name="ck_internships_duration_min",
        ),
        CheckConstraint(
            "duration_max_weeks IS NULL OR duration_max_weeks > 0",
            name="ck_internships_duration_max",
        ),
        CheckConstraint(
            "duration_min_weeks IS NULL OR duration_max_weeks IS NULL "
            "OR duration_min_weeks <= duration_max_weeks",
            name="ck_internships_duration_order",
        ),
        Index("ix_internships_company_id", "company_id"),
    )

    id = Column(Integer, primary_key=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id", ondelete="RESTRICT"),
    )

    source = Column(
        enum_column(Source, "ck_internships_source"),
        nullable=False,
    )

    external_id = Column(Text)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    work_model = Column(
        enum_column(WorkModel, "ck_internships_work_model")
    )

    duration_min_weeks = Column(Integer)
    duration_max_weeks = Column(Integer)

    compensation_status = Column(
        enum_column(
            CompensationStatus,
            "ck_internships_compensation_status",
        )
    )

    start_date = Column(Date)
    application_url = Column(Text)

    company = relationship(
        "Company",
        back_populates="internships",
    )

    categories = relationship(
        "Category",
        secondary="internship_categories",
        back_populates="internships",
        passive_deletes=True,
    )

    favorites = relationship(
        "Favorite",
        back_populates="internship",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    slug = Column(Text, unique=True, nullable=False)
    name = Column(Text, nullable=False)

    internships = relationship(
        "Internship",
        secondary="internship_categories",
        back_populates="categories",
        passive_deletes=True,
    )


class InternshipCategory(Base):
    __tablename__ = "internship_categories"

    __table_args__ = (
        Index("ix_internship_categories_category_id", "category_id"),
    )

    internship_id = Column(
        Integer,
        ForeignKey("internships.id", ondelete="CASCADE"),
        primary_key=True,
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Favorite(Base):
    __tablename__ = "favorites"

    __table_args__ = (
        Index("ix_favorites_internship_id", "internship_id"),
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )

    internship_id = Column(
        Integer,
        ForeignKey("internships.id", ondelete="CASCADE"),
        primary_key=True,
    )

    user = relationship(
        "User",
        back_populates="favorites",
    )

    internship = relationship(
        "Internship",
        back_populates="favorites",
    )