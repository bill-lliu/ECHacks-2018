from flask import render_template, jsonify, request
import core
from .app import app
import config


@app.before_first_request
def before_first_request():
    core.populate_database()


@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():
    return "Homepage"


@app.route("/about")
def about_page():
    return "About this project"


@app.route("/api", methods=["GET", "POST"])
def return_json():
    pass