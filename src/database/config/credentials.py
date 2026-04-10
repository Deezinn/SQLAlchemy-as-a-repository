from pydantic import BaseModel

from dotenv import load_dotenv

import os

load_dotenv()

class Credentials(BaseModel):
    url: str

    @staticmethod
    def build_url():

        dialect = os.getenv("DB_DIALECT")
        if not dialect:
            return "sqlite:///estudo.db"

        db_driver = os.getenv('DB_DRIVER')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_USER')
        db_pass = os.getenv('DB_PASS')

        driver_part = f"{dialect}+{db_driver}://"
        auth_part = f'{db_host}:{db_pass}@'
        database_part = f'{db_name}/{db_port}'

        return f'{driver_part}{auth_part}{database_part}'

credentials = Credentials(url=Credentials.build_url()).model_dump()
