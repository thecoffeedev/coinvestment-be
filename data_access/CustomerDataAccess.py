from flaskext.mysql import MySQL
from decouple import config  # for environment variables
from models.Customer import Customer
from models.Utility import Utility


class CustomerDataAccess:

    def __init__(self, app):
        self.mysql = MySQL()
        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
        app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
        self.mysql.init_app(app)

    def createTables(self):
        createTableQuery = "CREATE TABLE IF NOT EXISTS Customer (" \
                            "CustomerID VARCHAR(20), " \
                            "PasswordHash VARCHAR(60), " \
                            "RegisterDatetime FLOAT(53), " \
                            "EmailAddress VARCHAR(256), " \
                            "PreviousSignInDatetime FLOAT(53), " \
                            "CurrentSignInDatetime FLOAT(53), " \
                            "Name VARCHAR(256)" \
                            ")"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createTableQuery)
        cur.close()
        con.close()

    def createCustomer(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute('INSERT INTO Customer (CustomerID, PasswordHash, RegisterDatetime '
                    'EmailAddress, PreviousSignInDatetime, CurrentSignInDatetime, Name) '
                    'VALUES(%s,  %s, %s, %s,  %s, %s, %s)',
                    (customerObj.getCustomerID(), customerObj.getPasswordHash(),
                     customerObj.getRegisterDatetime, customerObj.getEmailAddress(),
                     customerObj.getPreviousSignInDatetime(), customerObj.getCurrentSignInDatetime(),
                     customerObj.getName()))
        cur.close()
        con.commit()
        con.close()


    def isExisting(self, emailAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Customer WHERE emailAddress = %s", emailAddress)
        entry = cur.fetchall()
        cur.close()
        con.close()

        # Empty cursor is False
        if entry:
            return True
        else:
            # If not existing return False
            return False

    def readCustomer(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Customer WHERE emailAddress = %s", customerObj.getEmailAddress())
        result = cur.fetchone()
        cur.close()
        con.commit()
        con.close()

        customer = Customer()
        customer.setCustomerID(result[0])
        customer.setPasswordHash(result[1])
        customer.setRegisterDatetime(result[2])
        customer.setEmailAddress(result[3])
        customer.setPreviousSignInDatetime(result[4])
        customer.setCurrentSignInDatetime(result[5])
        customer.setName(result[6])

    def updateCustomer(self, customerObj):
        pass




"""
        cur.execute('INSERT INTO user (username, email, password)VALUES( %s,  %s, %s)',
                        (username, email, password))

        con.commit()

"""

