from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from src.database.schemas.consulta import ConsultaSchema

from .base import Base


class VeterinarioSchema(Base):
    __tablename__ = "veterinario"

    id: Mapped[int] = mapped_column(primary_key=True)
    especialidade: Mapped[str] = mapped_column(String(25), nullable=False)

    consultas: Mapped[list["ConsultaSchema"]] = relationship(
        back_populates="veterinario", cascade="all, delete-orphan"
    )
