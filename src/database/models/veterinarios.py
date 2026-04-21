from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class VeterinariosModel(Base):
    __tablename__ = "veterinarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    especialidade: Mapped[str] = mapped_column(String(100), nullable=False)
