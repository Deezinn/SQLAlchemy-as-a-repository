from sqlalchemy.types import DateTime, String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ConsultaSchema(Base):
    __tablename__ = "consulta"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[DateTime] = mapped_column(DateTime())
    descricao: Mapped[str] = mapped_column(String(30), nullable=True)
