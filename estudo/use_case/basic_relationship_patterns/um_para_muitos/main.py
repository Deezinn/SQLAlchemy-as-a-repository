from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from estudo.use_case.basic_relationship_patterns.declarative_imperative.base import Base

# Um para muitos relacionamento coloca uma chave estrangeira na mesa de criança referenciando O pai.
# relationship()é então especificado no pai, como referenciando uma coleção de itens representados pela criança:


class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List["Child"]] = relationship(back_populates="parent", cascade="all, delete-orphan", single_parent=True) # coleção de items representados pela criança (classe child)



class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id", ondelete='CASCADE')) # child fazendo referencia a Parent (classe pai)
    parent: Mapped["Parent"] = relationship(back_populates="children")
