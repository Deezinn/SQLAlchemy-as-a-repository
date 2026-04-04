from sqlalchemy import delete, update

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import Address, User

stmt = delete(User).where(User.name == "Patrick")

print(stmt)

delete_stmt = (
               delete(User)
               .where(User.id == Address.id)
               .where(Address.email_address == "patrick@aol.com")
               )

from sqlalchemy.dialects import mysql

print(delete_stmt.compile(dialect=mysql.dialect()))


with engine.begin() as conn:
    result = conn.execute(
        update(User)
        .values(fullname="Patrick McStart")
        .where(User.name == "patrick")
    )
    print(result.rowcount)

print("")

update_stmt = (
    update(User)
    .where(User.name == "patrick")
    .values(fullname="Patrick the start")
    .returning(User.id, User.name)
)

print(update_stmt)

delete_stmt = (
    delete(User)
    .where(User.name == "patrick")
    .returning(User.id == User.name)
)

print(delete_stmt)
