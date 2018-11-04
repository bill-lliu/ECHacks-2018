from server.app import db
from server.models import Location


def populate_database():
    # db.session.add(Location object here)
    db.session.commit()
