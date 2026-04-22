from typing import List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from database.models.clientes import ClientesModel
from database.models.consultas import ConsultasModel
from database.models.prontuarios import ProntuariosModel


class PetsModel(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    especie: Mapped[str] = mapped_column(String(100),  nullable=False)
    idade: Mapped[int] = mapped_column(Integer(), nullable=False)

    cliente_id: Mapped[int] = mapped_column(ForeignKey('clientes.id', ondelete="CASCADE"), nullable=False)
    cliente: Mapped["ClientesModel"] = relationship(back_populates="pets")

    consultas: Mapped[List["ConsultasModel"]] = relationship(back_populates="pet", cascade="all, delete-orphan")

    prontuario: Mapped["ProntuariosModel"] = relationship(back_populates="pet", uselist=False, cascade="all, delete-orphan")
