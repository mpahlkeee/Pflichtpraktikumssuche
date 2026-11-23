import os
from pathlib import Path

from flask import Flask, render_template

import db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=Path(app.root_path) / "database.db",
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )
    db.init_app(app)

    @app.get("/")
    def index():
        return render_template("index.html")

    # Register feature blueprints here as they become available.
    return app
