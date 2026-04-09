from sqlalchemy.types import String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ProntuarioSchema(Base):
    __tablename__ = "prontuario"

    id: Mapped[int] = mapped_column(primary_key=True)
    historico_medico: Mapped[str] = mapped_column(String(15), nullable=False)
