from sqlalchemy.types import String

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class ClienteSchema(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(35), nullable=False)
    telefone: Mapped[str] = mapped_column(String(length=15), nullable=False)
    pets: Mapped[list["PetSchema"]] = relationship(  # type: ignore # noqa: F821
        back_populates="cliente", cascade="all, delete-orphan"
    )
