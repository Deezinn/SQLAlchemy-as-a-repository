from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

# from database.models.pets import PetsModel


class ProntuariosModel(Base):
    __tablename__ = "prontuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    historico_medico: Mapped[str] = mapped_column(String(100), nullable=False)

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    pet: Mapped["PetsModel"] = relationship(back_populates="prontuario")
