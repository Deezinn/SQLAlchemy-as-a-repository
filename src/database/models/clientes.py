
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class ClientesModel(Base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    
