from typing import Tuple

from sqlalchemy import Row, literal_column, select, text
from sqlalchemy.orm import Session

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import Address, User

stmt = select(User).where(User.name == "spongebob")

# print(stmt)


# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)

# with Session(engine) as session:
#     for row in session.execute(stmt):
#         print(row)


# print(select(User.name, User.fullname))

# # ou

# print(select(User["name", "fullname"]))

# print(select(User))

# with Session(engine) as session:
#     row: Row[Tuple[User]] | None = session.execute(select(User)).first()
#     print(row)
#     print(row[0])
#     user = session.scalars(select(User)).first()
#     print(user)

# print(select(User.name, User.fullname))

# with Session(engine) as session:
#     row = session.execute(select(User.name, User.fullname)).fetchmany()
#     print(row)

# with Session(engine) as session:
#     result = session.execute(
#         select(User.name, Address)
#         .where(User.id == Address.user_id)
#         .order_by(Address.id)
#     ).all()
#     print(result)

from sqlalchemy import func, cast

# stmt = select(
#     ("Username: " + User.name).label("username")
# ).order_by(User.name)

# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row.username)

# stmt = select(text("'some phrase'"), User.name).order_by(User.name)

# with engine.connect() as conn:
#     print(conn.execute(stmt).all())

# stmt = select(literal_column("'some phrase'").label('p'),
#               User.name).order_by(User.name)

# with engine.connect() as conn:
#     result = conn.execute(stmt).all()
#     print(result)

# print(User.name == "squidward")

# print(Address.user_id > 10)

# print(select(User).where(User.name == "squidward"))

# print(select(Address.email_address)
#       .where(User.name == "squidward")
#       .where(Address.user_id == User.id))

from sqlalchemy import and_, or_

# with engine.connect() as conn:

#     print(
#         conn.execute(
#             select(Address.email_address).where(
#                 and_(
#                     or_(User.name == "squidward", User.name == "sandy"),
#                     Address.user_id == User.id,
#                 )
#             )
#         )
#     )


# with engine.connect() as conn:
#     print(
#         conn.execute(
#             select(Address.email_address).where(
#                 or_(
#                     User.name == "squidward",
#                     and_(Address.user_id == User.id, User.name == "sandy"),
#                 )
#             )
#         )
#     )

with engine.connect() as conn:
    print(conn.execute(
        select(User).filter_by(name="spongebob", fullname="Spongebob squarepants")
    ).all())
