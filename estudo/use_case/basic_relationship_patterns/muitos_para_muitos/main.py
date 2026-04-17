from __future__ import annotations

from typing import Optional
from typing import List

from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

# class Base(DeclarativeBase):
#     pass

# association_table = Table(
#     "association_table",
#     Base.metadata,
#     Column("left_id", ForeignKey("left_table.id"), primary_key=True),
#     Column("right_id", ForeignKey("right_table.id"), primary_key=True)
# )

# class Parent(Base):
#     __tablename__ = "left_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[list[Child]] = relationship(back_populates="parents",secondary=association_table)

# class Child(Base):
#     __tablename__ = "right_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     parents: Mapped[list[Parent]] = relationship(back_populates="children", secondary=association_table)

class Base(DeclarativeBase):
    pass


class Association(Base):
    __tablename__ = "association_table"
    left_id: Mapped[int] = mapped_column(ForeignKey("left_table.id"), primary_key=True)
    right_id: Mapped[int] = mapped_column(
        ForeignKey("right_table.id"), primary_key=True
    )
    extra_data: Mapped[Optional[str]]
    child: Mapped["Child"] = relationship()


class Parent(Base):
    __tablename__ = "left_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Association"]] = relationship()


class Child(Base):
    __tablename__ = "right_table"
    id: Mapped[int] = mapped_column(primary_key=True)
