from flask import Flask
import flask_bootstrap
from .models import Base, engine
from flask_sqlalchemy import SQLAlchemy
import config

# Monkey-patch of flask_bootstrap to change bootstrap/jquery/html versions, may lead to problems
flask_bootstrap.BOOTSTRAP_VERSION = "4.1.0"
flask_bootstrap.JQUERY_VERSION = "3.3.1"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

flask_bootstrap.Bootstrap(app)
db = SQLAlchemy(app, metadata=Base.metadata)

import server.views
