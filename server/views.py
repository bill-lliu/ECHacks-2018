from flask import render_template
from .app import app
import config


@app.route("/")
@app.route("/home")
@app.route("/index")
def home_page():
    return "Homepage"


@app.route("/about")
def about_page():
    return "About this project"
