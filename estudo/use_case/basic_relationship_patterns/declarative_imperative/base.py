from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# class Parent(Base):
#     __tablename__ = "parent_table"

#     id = mapped_column(Integer, primary_key=True)
#     children = relationship("Child", collection_class=set, ...)
