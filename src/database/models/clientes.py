
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class ClientesModel(Base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    telefone: Mapped[str] = mapped_column(String(11), nullable=False)
