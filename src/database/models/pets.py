from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class PetsModel(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    especie: Mapped[str] = mapped_column(String(100),  nullable=False)
    idade: Mapped[int] = mapped_column(Integer(), nullable=False)
    
