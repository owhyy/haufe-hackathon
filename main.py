import datetime
from bottle import route, run, template

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.models import Base, Thing, User, Party


def _create_a_party(s: Session):
    admin = User(
        username="jojo",
        is_admin=True,
    )
    joe = User(
        username="joe",
    )
    alcohol = Thing(
        price=2000,
        name="Alcohol",
        description="Something to warm your soul",
        responsible=joe,
    )
    party = Party(
        name="halloween party 2024",
        max_budget=4000,
        date=datetime.date(2024, 10, 26),
        code="aaa111",
        users=[admin, joe],
    )

    s.add_all([admin, joe, alcohol, party])
    s.commit()


@route("/new-party")
def new_party():
    return template("new_party")


@route("/")
def main_page():
    return template("main_page")


if __name__ == "__main__":
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        _create_a_party(s)

    run(host="localhost", port=8080, debug=True, reloader=True)
