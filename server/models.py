from .app import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.String(4096), nullable=False)
    location = db.Column(db.String(1024), unique=True, nullable=False)
    long = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return '<Location %s>' % self.name
