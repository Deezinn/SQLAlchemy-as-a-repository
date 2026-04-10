from src.database.connection import engine

from .repository.clientes import ClienteRepository
from .schemas.base import Base

Base.metadata.create_all(bind=engine)
cr = ClienteRepository().insert(context={"nome": "andré", "telefone": "(81) 981873605"})

