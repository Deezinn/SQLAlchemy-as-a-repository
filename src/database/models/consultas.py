from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

# from database.models.pagamentos import PagamentosModel
# from database.models.pets import PetsModel
# from database.models.veterinarios import VeterinariosModel


class ConsultasModel(Base):
    __tablename__ = "consultas"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    descricao: Mapped[str] = mapped_column(String(100), nullable=False)

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id", ondelete="CASCADE"), nullable=False
    )
    pet: Mapped["PetsModel"] = relationship(back_populates="consultas")

    veterinario_id: Mapped[int] = mapped_column(
        ForeignKey("veterinarios.id", ondelete="CASCADE"), nullable=False
    )
    veterinario: Mapped["VeterinariosModel"] = relationship(back_populates="consultas")

    pagamento: Mapped["PagamentosModel"] = relationship(
        back_populates="consulta", uselist=False
    )
