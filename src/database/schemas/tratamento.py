from sqlalchemy.types import String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TratamentoSchema(Base):
    __tablename__ = "tratamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30), nullable=False)
    descricao: Mapped[str] = mapped_column(String(30), nullable=False)
