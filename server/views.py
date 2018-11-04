from flask import render_template, request
import core
from .app import app, db
from .models import Location
import config


@app.before_first_request
def before_first_request():
    core.populate_database()


@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():
    categories = [i.category for i in db.session.query(Location.category).distinct().all()]
    return render_template("index.jinja2", categories=categories)


@app.route("/about")
def about_page():
    return "About this project"


@app.route("/api", methods=["GET", "POST"])
def return_json():
    long = request.args.get("long")
    lat = request.args.get("lat")
    category = request.args.get("category")

    # print(long, lat, category)

    response = {"Locations": []}

    for location in (
        db.session.query(Location).filter(Location.category == category).all()
    ):
        response["Locations"].append(
            {
                "id": location.id,
                "name": location.name,
                "description": location.description,
                "long": location.long,
                "lat": location.lat,
                "category": location.category,
            }
        )

    return str(response).replace("\'", "\"")
