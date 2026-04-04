
from sqlalchemy import bindparam, update, select

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import Address, User

# stmt = (
#     update(User)
#     .where(User.name == "patrick")
#     .values(fullname="Patrick the start")
# )

# print(stmt)

# stmt = update(User).values(fullname="Username= " + User.name)
# print(stmt)

# stmt = (
#     update(User)
#     .where(User.name == bindparam("oldname"))
#     )

# with engine.begin() as conn:
#     conn.execute(
#         stmt,
#         [
#             {"oldname": "jack", "newname": "ed"},
#             {"oldname": "wendy", "newname": "mary"},
#             {"oldname": "jim", "newname": "jake"},
#         ],
#     )

# scalart_subq = (
#     select(Address.email_address)
#     .where(Address.user_id == User.id)
#     .order_by(Address.id)
#     .limit(1)
#     .scalar_subquery()
# )

# update_stmt = update(User).values(fullname=scalart_subq)
# print(update_stmt)

# update_stmt= (
#     update(User)
#     .where(User.id == Address.id)
#     .where(Address.email_address == "patrick@aol.com")
#     .values(fullname="Pat")
# )
# print(update_stmt)

# update_stmt = (
#     update(User)
#     .where(User.id == Address.user_id)
#     .where(Address.email_address == "patrick@aol.com")
#     .values(
#         {
#             User.fullname: "Pat",
#             Address.email_address: "pat@aol.com",
#         }
#     )
# )

# from sqlalchemy.dialects import mysql

# print(update_stmt.compile(dialect=mysql.dialect()))

from sqlalchemy import Values

values = Values(
    User.id,
    User.name,
    name="my_values",
).data(
    [(1,"new_name"), (2, "another_name"), (3, "name_name")]
)

update_stmt = (
    update(User).values(name=values.c.name).where(User.id == values.c.id)
)

from sqlalchemy.dialects import postgresql

print(update_stmt.compile(dialect=postgresql.dialect()))
