from flask import current_app, g
from sqlalchemy import URL, create_engine, event
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import sessionmaker

from models import Base, Category
from values import CATEGORIES


def get_db():
    if "db_session" not in g:
        g.db_session = current_app.extensions["db_session_factory"]()

    return g.db_session


def close_db(error=None):
    session = g.pop("db_session", None)

    if session is not None:
        session.close()


def init_app(app):
    url = URL.create("sqlite+pysqlite", database=str(app.config["DATABASE"]))
    engine = create_engine(url)

    @event.listens_for(engine, "connect")
    def enable_foreign_keys(connection, record):
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    app.extensions["db_engine"] = engine
    app.extensions["db_session_factory"] = sessionmaker(engine)
    app.teardown_appcontext(close_db)

    Base.metadata.create_all(engine)

    statement = insert(Category).values(
        [{"slug": slug, "name": name} for slug, name in CATEGORIES]
    )

    with engine.begin() as connection:
        connection.execute(
            statement.on_conflict_do_nothing(index_elements=["slug"])
        )