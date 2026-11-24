import os
from pathlib import Path

from flask import Flask, render_template

import db


def create_app():
    app = Flask(__name__)

    app.config["DATABASE"] = Path(app.root_path) / "database.db"

    db.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/praktika")
    def praktika():
        return render_template("praktika.html")

    @app.route("/favoriten")
    def favoriten():
        return render_template("favoriten.html")

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route("/register")
    def register():
        return render_template("register.html")

    return app


app = create_app()
