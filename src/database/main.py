from src.database.connection import engine

from .repository.clientes import ClienteRepository
from .schemas.base import Base

Base.metadata.create_all(bind=engine)
