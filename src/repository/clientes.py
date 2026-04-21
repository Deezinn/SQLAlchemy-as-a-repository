from sqlalchemy import insert
from src.database.connection.engine import engine
from schemas import ClienteSchema

class ClienteRepository:

    def insert(self, context) -> None:

        stmt = insert(ClienteSchema).values(context)
        with engine.begin() as conn:
            conn.execute(statement=stmt)

