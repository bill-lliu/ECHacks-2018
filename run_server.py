from server.app import app, db
from server.models import Refugee, HostFamily


def populate_database():
    db.create_all()
    db.session.add(Refugee(refugee_id=1, name="Guy Morgenshtern", age=17, primary_language="English", secondary_language="Also English", family_size = 1, previous_occupation="Food eater"))
    db.session.add(HostFamily(host_id=1, name="Bill Liu", age=17, primary_language="English", secondary_language="Also English", available_space=10, occupation="Hackerman", salary=100000000, location="Canada"))
    db.session.commit()


if __name__ == "__main__":
    # populate_database()
    app.run()