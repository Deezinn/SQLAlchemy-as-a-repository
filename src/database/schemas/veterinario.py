from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class VeterinarioSchema(Base):
    __tablename__ = 'veterinario'

    id: Mapped[int] = mapped_column(primary_key=True)
    especialidade: Mapped[str] = mapped_column(String(25), nullable=False)
