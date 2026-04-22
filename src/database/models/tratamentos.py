from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

# from database.models.pets import PetsModel


class TratamentosModel(Base):
    __tablename__ = "tratamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(100), nullable=False)

    pets: Mapped[List["PetsModel"]] = relationship(
        secondary="pet_tratamentos", back_populates="tratamentos"
    )
