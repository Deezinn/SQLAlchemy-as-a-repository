from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String

# from src.database.schemas.pet import PetSchema

from .base import Base


class ProntuarioSchema(Base):
    __tablename__ = "prontuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    historico_medico: Mapped[str] = mapped_column(String(15), nullable=False)

    pet_id: Mapped[int] = mapped_column(ForeignKey("pet.id"), nullable=False, unique=True)
    pet: Mapped["PetSchema"] = relationship(
        back_populates="prontuario", cascade="all, delete-orphan"
    )
