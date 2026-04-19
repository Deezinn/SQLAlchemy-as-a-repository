from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime, String

# from src.database.schemas.pagamento import PagamentoSchema
# from src.database.schemas.pet import PetSchema
# from src.database.schemas.veterinario import VeterinarioSchema

from .base import Base


class ConsultaSchema(Base):
    __tablename__ = "consulta"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[DateTime] = mapped_column(DateTime())
    descricao: Mapped[str] = mapped_column(String(30), nullable=True)

    pet_id: Mapped[int] = mapped_column(ForeignKey('pet.id'))
    pet: Mapped["PetSchema"] = relationship(
        back_populates="consultas"
    )

    veterinario_id: Mapped[int] = mapped_column(
        ForeignKey("veterinario.id"), nullable=False
    )
    veterinario: Mapped["VeterinarioSchema"] = relationship(
        back_populates="consultas"
    )

    pagamento: Mapped["PagamentoSchema"] = relationship(
        back_populates="consulta", cascade="all, delete-orphan", uselist=False
    )
