import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")
DATABASE_URL = "sqlite:///" + os.path.join(DATA_FOLDER, "webapp.db")
