from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base

# from database.models.consultas import ConsultasModel


class PagamentosModel(Base):
    __tablename__ = "pagamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(100), nullable=False, default="ativo")

    consulta_id: Mapped[int] = mapped_column(
        ForeignKey("consultas.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    consulta: Mapped["ConsultasModel"] = relationship(back_populates="pagamento")
