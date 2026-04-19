from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Integer, String

# from src.database.schemas.consulta import ConsultaSchema
# from src.database.schemas.prontuario import ProntuarioSchema

from .base import Base


class PetSchema(Base):
    __tablename__ = "pet"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), nullable=False)
    especie: Mapped[str] = mapped_column(String(20), nullable=False)
    idade: Mapped[int] = mapped_column(Integer(), nullable=True)

    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False)
    cliente: Mapped["ClienteSchema"] = relationship(
        back_populates="pets"
    )  # type: ignore # noqa: F821

    consultas: Mapped[list["ConsultaSchema"]] = relationship(
        back_populates="pet", cascade="all, delete-orphan"
    )

    prontuario: Mapped["ProntuarioSchema"] = relationship(
        back_populates="pet", uselist=False, cascade="all, delete-orphan"
    )
