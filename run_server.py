from server.app import app, db
from server.models import Refugee, HostFamily


def populate_database():
    db.create_all()
    db.session.add(Refugee(refugee_id=1, name="Guy Morgenshtern", age=17, primary_language="English", secondary_language="Also English", family_size = 1, previous_occupation="Food eater"))
    db.session.add(HostFamily(host_id=1, name ="Refugee 1", age=24, primary_language="English", secondary_language="", available_space=3, family_size=2, occupation="Electrician", salary=70000, location="Toronto"))
    db.session.commit()


if __name__ == "__main__":
    populate_database()
