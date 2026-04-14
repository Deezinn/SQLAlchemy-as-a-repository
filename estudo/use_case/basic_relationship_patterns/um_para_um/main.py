from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from estudo.use_case.basic_relationship_patterns.declarative_imperative.base import Base


class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    #relationship
    child: Mapped["Child"] = relationship(back_populates="parent", uselist=False)

# class Child(Base):
#     __tablename__ = "child_table"

#     id: Mapped[int] = mapped_column(primary_key=True)

#     parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
#     parent: Mapped["Parent"] = relationship(back_populates="child", single_parent=True) #Parametro que transforma em 1:1

class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="child")

    __table_args__ = (UniqueConstraint("parent_id"))
