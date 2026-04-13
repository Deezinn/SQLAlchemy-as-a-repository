from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from estudo.use_case.basic_relationship_patterns.declarative_imperative.base import Base

# Muitos para um coloca uma chave estrangeira na tabela de pais que faz referência à criança.
# relationship() é declarado no pai, onde uma nova retenção escalar atributo será criado:

# class Parent(Base):
#     __tablename__ = "parent_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
#     child: Mapped["Child"] = relationship(back_populates="parents")

# class Child(Base):
#     __tablename__ = "child_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     parents: Mapped[List["Parent"]] = relationship(back_populates="child")

# Nullable muitos para um ( N:1 )

from typing import Optional

class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    child_id: Mapped[int | None] = mapped_column(ForeignKey("child_table.id"))
    child: Mapped[Optional["Child"] | None] = relationship(back_populates="children")

class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)

    parents: Mapped[List["Parent"]] = relationship(back_populates="child")
