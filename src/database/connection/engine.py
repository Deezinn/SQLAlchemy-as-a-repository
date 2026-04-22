from sqlalchemy import Engine, create_engine

from database.config.credentials import credentials

engine: Engine = create_engine(
    url=credentials["url"],
)
