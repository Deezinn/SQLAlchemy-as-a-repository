from database.models.base import Base
from database.connection import engine

Base.metadata.create_all(engine)
