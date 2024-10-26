import datetime
from bottle import route, run, template, abort, request, post, patch

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
    billie = User(
        username="bill",
    )
    party = Party(
        name="halloween party 2024",
        max_budget=4000,
        date=datetime.date(2024, 10, 26),
        code="aaa111",
        users=[admin, joe, billie],
    )
    alcohol = Thing(
        price=2000,
        name="Alcohol",
        description="Something to warm your soul",
        responsible=joe,
        party=party,
    )
    location = Thing(
        price=500,
        name="Location",
        description="Rent",
        responsible=joe,
        party=party,
    )
    dj = Thing(
        price=500,
        name="DJ",
        description="For the muzak",
        responsible=billie,
        party=party,
    )
    snacks = Thing(price=150, name="Snacks", description="Snacky snacks", responsible=admin, party=party)

    s.add_all([admin, joe, billie, alcohol, location, dj, snacks, party])
    s.commit()


@route("/new-party")
def new_party():
    return template("new_party")


@route("/get-party")
def get_party():
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


@patch("/party/<party_id>/reassign/<thing_id>")
def reassign_thing(party_id: int, thing_id: int):
    stmt = select(Party).where(Party.id == int(party_id))
    party = s.scalar(stmt)

    if not party:
        abort(404, "Party not found")

    try:
        thing = next(t for t in party.things if t.id == int(thing_id))
    except StopIteration:
        abort(404, "Thing not found")

    try:
        user = next(u for u in party.users if u.id == int(request.POST.responsible))
    except StopIteration:
        abort(404, "User not found or isn't in this party planning session")

    thing.user_id = user.id
    s.commit()

    users_except_assigned = filter(lambda u: u.id != user.id, party.users)
    return f'<option selected value="{user.id}">{user.username}</option>' + "".join(
        f'<option value="{u.id}">{u.username}</option>' for u in users_except_assigned
    )


@route("/")
def main_page():
    return template("main_page")


if __name__ == "__main__":
    with Session(engine) as s:
        _create_a_party(s)

    run(host="localhost", port=8080, debug=True, reloader=True)
