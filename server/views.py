from .app import app, db
from .models import HostFamily
from flask import render_template


@app.route("/")
def index():
    return render_template("index.jinja2")


# Example for Guy
@app.route("/compatibility/<int:refugee_id>")
def compatibility(refugee_id: int):
    string = ""
    for family in db.session.query(HostFamily).all():
        string += family.name
    return string
