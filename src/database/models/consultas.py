from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class ConsultasModel(Base):
    __tablename__ = "consultas"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    descricao: Mapped[str] = mapped_column(String(), nullable=False)
