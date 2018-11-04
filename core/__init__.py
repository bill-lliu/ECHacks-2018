from server.app import db
from server.models import Location


def populate_database():

    db.session.commit()
