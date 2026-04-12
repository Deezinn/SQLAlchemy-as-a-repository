
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import User


with Session(engine) as session:
    for user_obj in session.execute(
        select(User).options(selectinload(User.addresses))
    ).scalars():
        print(user_obj.addresses)

# evitando problema n + 1
