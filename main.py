import datetime
from bottle import route, run, template, abort, request, post

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db.models import Base, Thing, User, Party

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)


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


@route("/get-party")
def get_party():
    # return 200 if party exists, as well as tepmlate + embed code in it
    # return 404 if it doesn't

    # TODO(ion): add layer on top of orm that will make the requests
    stmt = select(Party).where(Party.code == request.params.code)
    party = s.scalar(stmt)
    if not party:
        abort(404, "A party with this code was not found")

    return template("join_party", party=party)


@post("/party/<code>/join")
def join_party(code: str):
    stmt = select(Party).where(Party.code == code)
    party = s.scalar(stmt)
    username = request.POST.username

    try:
        user = next(u for u in party.users if u.username == username)
    except StopIteration:
        user = User(username=username, party=party)
        s.add(user)
        s.commit()

    return template("get_party", party=party, user=user)


@route("/")
def main_page():
    return template("main_page")


if __name__ == "__main__":
    with Session(engine) as s:
        _create_a_party(s)

    run(host="localhost", port=8080, debug=True, reloader=True)
