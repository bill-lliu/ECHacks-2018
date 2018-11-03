from server.app import app, db
from server.models import Refugee, HostFamily


def populate_database():
    db.create_all()

    db.session.add(
        Refugee(
            refugee_id=1,
            name="Ref 1",
            age=17,
            primary_language="English",
            secondary_language="",
            family_size=1,
            previous_occupation="Food eater",
        )
    )

    db.session.add(
        Refugee(
            refugee_id=2,
            name="Ref 2",
            age=25,
            primary_language="English",
            secondary_language="Japanese",
            family_size=2,
            previous_occupation="Farmer",
        )
    )

    db.session.add(
        Refugee(
            refugee_id=3,
            name="Ref 3",
            age=30,
            primary_language="English",
            secondary_language="Hindi",
            family_size=3,
            previous_occupation="unemployed",
        )
    )

    db.session.add(
        Refugee(
            refugee_id=4,
            name="Ref 4",
            age=64,
            primary_language="Hindi",
            secondary_language="French",
            family_size=5,
            previous_occupation="Engineer",
        )
    )

    db.session.add(
        Refugee(
            refugee_id=5,
            name="Ref 5",
            age=19,
            primary_language="Swahili",
            secondary_language="",
            family_size=1,
            previous_occupation="Electrician",
        )
    )

    db.session.add(
        HostFamily(
            host_id=1,
            name="Host 1",
            age=17,
            primary_language="English",
            secondary_language="",
            available_space=10,
            occupation="unemployed",
            salary=100000,
            location="Canada",
        )
    )

    db.session.add(
        HostFamily(
            host_id=2,
            name="Host 2",
            age=17,
            primary_language="Spanish",
            secondary_language="English",
            available_space=10,
            occupation="Software Engineer",
            salary=50000,
            location="Canada",
        )
    )

    db.session.add(
        HostFamily(
            host_id=3,
            name="Host 3",
            age=17,
            primary_language="Spanish",
            secondary_language="",
            available_space=10,
            occupation="Electrician",
            salary=9000,
            location="Canada",
        )
    )

    db.session.add(
        HostFamily(
            host_id=4,
            name="Host 4",
            age=17,
            primary_language="Japanese",
            secondary_language="English",
            available_space=10,
            occupation="Nurse",
            salary=190000,
            location="Canada",
        )
    )

    db.session.add(
        HostFamily(
            host_id=5,
            name="Host 5",
            age=17,
            primary_language="Swahili",
            secondary_language="Hindi",
            available_space=10,
            occupation="Policeman",
            salary=100000000,
            location="Canada",
        )
    )

    db.session.commit()


if __name__ == "__main__":
    # populate_database()
    app.run()
