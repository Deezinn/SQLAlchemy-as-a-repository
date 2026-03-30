from sqlalchemy import Engine, create_engine
from .credentials import settings

url: dict[str,str] = settings.model_dump()

engine: Engine = create_engine(url=url['db_url'], echo=True, pool_recycle=3600)


