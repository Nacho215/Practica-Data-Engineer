from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

# Define declarative base needed for ORM
Base = declarative_base()


class Customer(Base):
    """
    Class representing 'customer' table.
    Its id and other attributes represents the table columns.

    Args:
        Base (Base): Declarative base needed for ORM.
    """
    __tablename__ = 'customer'
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)
    id = Column(Integer, primary_key=True)

    def __init__(self, name, age, email, address, zip_code) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

    def __repr__(self) -> str:
        return "<Customer(name='%s', age='%s', email='%s', address='%s', zip_code='%s')>" \
            % (self.name, self.age, self.email, self.address, self.zip_code)
