from .app import app, db
from .models import HostFamily


@app.route("/")
def index():
    return "Let's get this bread"


# Example for Guy
@app.route("/compatibility/<int:refugee_id>")
def compatibility(refugee_id: int):
    string = ""
    for family in db.session.query(HostFamily).all():
        string += family.name
    return string
