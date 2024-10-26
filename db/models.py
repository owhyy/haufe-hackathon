from sqlalchemy import Boolean, Date, ForeignKey, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)
import datetime


class Base(DeclarativeBase):
    pass


class Party(Base):
    __tablename__ = "party"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    # TODO(ion): this could be an unsigned int; need to figure out a db-agnostic way to set it as this though
    max_budget: Mapped[int] = mapped_column(Integer)
    date: Mapped[datetime.date] = mapped_column(Date)
    code: Mapped[str] = mapped_column(String(10))

    users: Mapped[list["User"]] = relationship(
        back_populates="party", cascade="all, delete-orphan"
    )
    things: Mapped[list["Thing"]] = relationship(
        back_populates="party", cascade="all, delete-orphan"
    )

    @property
    def current_budget(self):
        return sum(t.price for t in self.things)


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(40))
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    party_id: Mapped[int] = mapped_column(ForeignKey("party.id"))

    party: Mapped["Party"] = relationship(back_populates="users")
    assigned_things: Mapped["Thing"] = relationship(
        back_populates="responsible", cascade="all, delete-orphan"
    )


class Thing(Base):
    __tablename__ = "thing"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(String(40))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    party_id: Mapped[int] = mapped_column(ForeignKey("party.id"))

    party: Mapped["Party"] = relationship(back_populates="things")
    responsible: Mapped["User"] = relationship(back_populates="assigned_things")
