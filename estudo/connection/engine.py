from sqlalchemy import Engine, create_engine
from .credentials import settings

url = settings.model_dump()

engine: Engine = create_engine(url=url['db_url'])

print(engine)
