from .app import app, db


@app.route("/")
def index():
    return "Let's get this bread"
