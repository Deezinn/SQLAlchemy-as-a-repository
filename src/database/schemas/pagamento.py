from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Boolean, Float

# from src.database.schemas.consulta import ConsultaSchema

from .base import Base


class PagamentoSchema(Base):
    __tablename__ = "pagamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[float] = mapped_column(Float(2))
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)

    consulta_id: Mapped[int] = mapped_column(ForeignKey("consulta.id"), unique=True)
    consulta: Mapped["ConsultaSchema"] = relationship(
        back_populates="pagamento"
    )
