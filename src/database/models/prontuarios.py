from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class ProntuariosModel(Base):
    __tablename__ = "prontuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    historico_medico: Mapped[str] = mapped_column(String(100), nullable=False)
