from sqlalchemy import select
from sqlalchemy.orm import Session

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import User

stmt = select(User).where(User.name == "spongebob")

print(stmt)


with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)


