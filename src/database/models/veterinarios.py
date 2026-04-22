from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

# from database.models.consultas import ConsultasModel


class VeterinariosModel(Base):
    __tablename__ = "veterinarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    especialidade: Mapped[str] = mapped_column(String(100), nullable=False)

    consultas: Mapped[List["ConsultasModel"]] = relationship(
        back_populates="veterinario", cascade="all, delete-orphan"
    )
