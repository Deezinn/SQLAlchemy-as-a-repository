from decimal import Decimal

from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class PagamentosModel(Base):
    __tablename__ = "pagamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    valor: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
