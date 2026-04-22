from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

# from src.database.models.pets import PetsModel


class ClientesModel(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    telefone: Mapped[str] = mapped_column(String(11), nullable=False)

    pets: Mapped[List["PetsModel"]] = relationship(
        back_populates="cliente", cascade="all, delete-orphan"
    )
