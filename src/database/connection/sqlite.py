from sqlalchemy import Engine, create_engine

from src.database.config.credentials import credentials

url_database = credentials.model_dump()

engine: Engine = create_engine(
    url=url_database["url"],
)

print(engine)
