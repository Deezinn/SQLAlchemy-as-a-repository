from sqlalchemy.orm import Mapped, Session, session
from sqlalchemy.orm import relationship

from estudo.connection import engine
from estudo.use_case.working_with_database_metadata.with_declarative_base import Address, Base, User

# class User(Base):
#     __tablename__ = "user_account"

#     addresses: Mapped[list["Address"]] = relationship(back_populates='user')

# class Address(Base):
#     __tablename__ = "address"

#     user: Mapped["User"] = relationship(back_populates="addresses")

u1 = User(name='pkrabs', fullname='Pearl Krabs')
print(u1)
print(u1.addresses)

a1 = Address(email_address='pearl.krabs@gmail.com')
u1.addresses.append(a1)

print(u1.addresses)
print(a1.user)

a2 = Address(email_address="pearl@aol.com", user=u1)
print(u1.addresses)

a2.user = u1
print(a2.user)

with Session(engine) as session:
    session.add(u1)
    print(u1 in session)
    print(a1 in session)
    print(a2 in session)
    session.commit()
    print(u1.id)
    print(u1.addresses)
    print("")
    print(a1)
    print(a2)
