from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .base import Base

# Mapped class
class Parent(Base):
    __tablename__: str = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Child"]] = relationship(back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")


# Sem Mapped class (annoted)
# class Parent(Base):
#     __tablename__: str = "parent_table"

#     id = mapped_column(Integer, primary_key=True)
#     children = relationship("Child", back_populates="parent")


# class Child(Base):
#     __tablename__ = "child_table"

#     id = mapped_column(Integer, primary_key=True)
#     parent_id = mapped_column(ForeignKey("parent_table.id"))
#     parent = relationship("Parent", back_populates="children")
