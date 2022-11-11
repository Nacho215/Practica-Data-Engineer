import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.orm import Session
import models

# Connection credentials
SQL_MOTOR = 'postgresql'
SQL_USER = 'nacho'
SQL_PASS = 'admin'
SQL_HOST = 'localhost'
SQL_DB = 'test'


class Database():
    """
    Class used to manage database connection, DDL and DML SQL sentences.
    """
    # Engine creation with given credentials
    engine = db.create_engine(f'{SQL_MOTOR}://{SQL_USER}:{SQL_PASS}@{SQL_HOST}/{SQL_DB}')

    def __init__(self) -> None:
        """
        When instantiated, connect to database, and store the connection.
        """
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQuery(self, query) -> None:
        """
        Fetches all data from a given query, and prints the results.

        Args:
            query (str): a valid SQL query for a FROM clause.
        """
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def fetchUserByName(self) -> None:
        """
        Fetches all data from column 'name' from table 'customers',
        and prints it in console.
        """
        meta = MetaData()
        customer = Table('customer', meta, Column('name'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)

    def fetchAllUsers(self) -> None:
        """
        Fetches all users info based on its __repr__ methods.
        """
        self.session = Session(bind=self.connection)
        customers = self.session.query(models.Customer).all()
        for cust in customers:
            print(cust)

    def saveData(self, customer) -> None:
        """
        Insert a given customer in 'customers' table.

        Args:
            customer (Customer): A valid Customer object.
        """
        session = Session(bind=self.connection)
        session.add(customer)
        session.commit()

    def updateCustomer(self, customerName, address) -> None:
        """
        Finds a Customer that matches the given customerName, and updates its address.

        Args:
            customerName (str): Customer's name to update.
            address (str): New address.
        """
        session = Session(bind=self.connection)
        dataToUpdate = {models.Customer.address: address}
        customerData = session.query(models.Customer).filter(models.Customer.name == customerName)
        customerData.update(dataToUpdate)
        session.commit()

    def deleteCustomer(self, customerName) -> None:
        """
        Deletes first Customer that matches given customerName.

        Args:
            customerName (str): Name of the Customer to delete.
        """
        session = Session(bind=self.connection)
        customerData = session.query(models.Customer).filter(models.Customer.name == customerName).first()
        session.delete(customerData)
        session.commit()


def main():
    database = Database()
    # new_customer = models.Customer('Martín Pérez', 30, 'randomEmail@gmail.com', 'randomAdress 123', '2600')
    # new_customer = models.Customer('Gonzalo Domínguez', 20, 'randomEmail2@gmail.com', 'randomAdress 888', 'SD34FG')
    # database.saveData(new_customer)
    # database.fetchByQuery('public.customer')
    database.fetchAllUsers()
    # database.updateCustomer('Martín Pérez', 'Real Address 456')
    # database.deleteCustomer('asd')


if __name__ == '__main__':
    main()
