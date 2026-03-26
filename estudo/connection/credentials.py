import os

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    db_url: str

    @staticmethod
    def build_db_url() -> str:

        dialect = os.getenv('DB_DIALECT')
        if not dialect:
            return 'sqlite://.local.db'

        driver = os.getenv(key="DB_DRIVER")
        host = os.getenv(key="DB_HOST")
        port = os.getenv(key="DB_PORT")
        name = os.getenv(key="DB_NAME")
        user = os.getenv(key="DB_USER")
        password = os.getenv(key="DB_PASS")


        driver_part = f'+{driver}' if driver else ""
        auth_part = f'{user}:{password}@' if user and password else ""
        host_part = f'{host}:{port}' if host and port else host

        return f"{dialect}{driver_part}://{auth_part}{host_part}/{name}"

settings = Settings(db_url=Settings.build_db_url())
print(settings)
