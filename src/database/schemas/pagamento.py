from sqlalchemy.types import Float, Boolean

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PagamentoSchema(Base):
    __tablename__ = "pagamento"

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[float] = mapped_column(Float(2))
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
