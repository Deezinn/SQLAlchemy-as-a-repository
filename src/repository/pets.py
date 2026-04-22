# from sqlalchemy import insert
# from src.database.connection.engine import engine
# from schemas import PetSchema


# class PetsRepository:
#     def insert(self, context) -> None:

#         stmt = insert(PetSchema).values(context)
#         with engine.begin() as conn:
#             conn.execute(statement=stmt)
