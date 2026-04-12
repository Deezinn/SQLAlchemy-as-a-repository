from sqlalchemy import select

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import Address, User


with engine.connect() as conn:
    result = conn.execute(select(Address.email_address).select_from(User).join(User.addresses))
    print(result.all())
    print("")
    result = conn.execute(select(Address.email_address).join_from(User, Address))
    print(result.all())
