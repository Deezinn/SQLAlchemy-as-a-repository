from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class PetTratamentoModel(Base):
    __tablename__ = "pet_tratamentos"

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id", ondelete="CASCADE"), primary_key=True
    )
    tratamento_id: Mapped[int] = mapped_column(
        ForeignKey("tratamentos.id", ondelete="CASCADE"), primary_key=True
    )
