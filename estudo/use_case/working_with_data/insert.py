from estudo import User, Address, engine

from sqlalchemy import insert, select

# compiled = stmt.compile()

# print(compiled.params)

# stmt = insert(User).values(name='spongebob', fullname="Spongebob squarepants")
# with engine.begin() as conn:
#     result = conn.execute(stmt)
#     print(result.inserted_primary_key)

# print(insert(User))

# with engine.begin() as conn:
#     result = conn.execute(insert(User), [
#         {"name": "sandy", "fullname": "sandy cheeks"},
#         {"name": "patrick", "fullname": "Patrick star"}
#     ])

# from sqlalchemy import select, bindparam

# scalar_subq = (
#     select(User.id)
#     .where(User.name == bindparam("username"))
#     .scalar_subquery()
# )

# with engine.begin() as conn:
#     result = conn.execute(
#         insert(Address).values(user_id=scalar_subq),
#         [
#             {"username": "spongebob", "email_address": "spongebob@sqlalchemy.org"},
#             {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
#             {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
#         ],
#     )

# print(insert(User).values().compile(engine))

# insert_stmt = insert(Address).returning(
#     Address.id, Address.email_address
# )

# print(insert_stmt)

select_stmt = select(User.id, User.name + "@aol.com")
insert_stmt = insert(Address).from_select(
    ["user_id", "email_address"], select_stmt
)
print(insert_stmt.returning(Address.id, Address.email_address))
print("")
print(insert_stmt)
