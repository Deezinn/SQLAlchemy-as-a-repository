from sqlalchemy import ForeignKey

from sqlalchemy.types import Integer, String

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class PetSchema(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), nullable=False)
    especie: Mapped[str] = mapped_column(String(20), nullable=False)
    idade: Mapped[int] = mapped_column(Integer(), nullable=True)

    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False)
    cliente: Mapped["ClienteSchema"] = relationship(back_populates="pets")   # type: ignore # noqa: F821


    #
