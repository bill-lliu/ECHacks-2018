from .app import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), unique=True, nullable=False)
    location = db.Column(db.String(1024), unique=True, nullable=False)

    def __repr__(self):
        return '<Location %s>' % self.name
