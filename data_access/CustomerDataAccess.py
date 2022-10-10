from flaskext.mysql import MySQL
from decouple import config  # for environment variables
from models.Customer import Customer


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
                            "RegisterDatetime INT, " \
                            "EmailAddress VARCHAR(256), " \
                            "PreviousSignInDatetime INT, " \
                            "CurrentSignInDatetime INT, " \
                            "Name VARCHAR(256)" \
                            ") DEFAULT COLLATE=utf8_bin"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createTableQuery)
        cur.close()
        con.close()

    def insertDayZeroData(self):
        con = self.mysql.connect()
        cur = con.cursor()

        # If the table exists and is empty, insert the customer models
        cur.execute("SELECT EXISTS (SELECT * FROM Customer)")

        if not cur.fetchone()[0]:
            customerOne = Customer()
            customerOne.setCustomerID("1WNJKpBpYfWwKIlvbaz0")
            customerOne.setPasswordHash("$2b$12$hilgtAM2h/10jUiOGpA.IuTq2vieG3A4o95kNiaUvsOnBjindoKMa")
            customerOne.setRegisterDatetime(1664471892)
            customerOne.setEmailAddress("beatrice.shilling@hotmail.com")
            customerOne.setPreviousSignInDatetime(1664567871)
            customerOne.setCurrentSignInDatetime(1664567244)
            customerOne.setName("Beatrice Shilling")

            customerTwo = Customer()
            customerTwo.setCustomerID("Debo32tKqJBeZwHHgkvx")
            customerTwo.setPasswordHash("$2b$12$GCq529ew5SSOUINxa.nxSOI27Ir1vIvww5X7go9eKysksavMCUL4a")
            customerTwo.setRegisterDatetime(1664281967)
            customerTwo.setEmailAddress("frank.whittle@yahoomail.com")
            customerTwo.setPreviousSignInDatetime(1664460752)
            customerTwo.setCurrentSignInDatetime(1664538380)
            customerTwo.setName("Frank Whittle")

            self.insertCustomer(customerOne)
            self.insertCustomer(customerTwo)

        cur.close()
        con.commit()
        con.close()

    def insertCustomer(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        insertQuery = "INSERT INTO Customer (" \
                      "CustomerID, PasswordHash, RegisterDatetime, EmailAddress, " \
                      "PreviousSignInDatetime, CurrentSignInDatetime, Name) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)"

        cur.execute(insertQuery, (customerObj.getCustomerID(), customerObj.getPasswordHash(),
                                  customerObj.getRegisterDatetime(), customerObj.getEmailAddress(),
                                  customerObj.getPreviousSignInDatetime(), customerObj.getCurrentSignInDatetime(),
                                  customerObj.getName()))

        cur.close()
        con.commit()
        con.close()

    def isCustomerExistingByEmailAddress(self, emailAddress):
        query = "SELECT * FROM Customer " \
                "WHERE EmailAddress = %s"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(query, emailAddress)
        rowCount = cur.rowcount
        entry = cur.fetchone()
        cur.close()
        con.close()

        # Empty cursor is False, therefore customer does not exist
        if rowCount:
            return True
        else:
            return False

    def isCustomerExistingByCustomerID(self, customerID):
        query = "SELECT * FROM Customer " \
                "WHERE CustomerID = %s"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(query, customerID)
        rowCount = cur.rowcount
        entry = cur.fetchone()
        cur.close()
        con.close()

        # Empty cursor is False, therefore customer does not exist
        if rowCount:
            return True
        else:
            return False

    def readCustomerByEmail(self, emailAddress):
        query = "SELECT * FROM Customer " \
                "WHERE EmailAddress = %s"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(query, emailAddress)
        rowCount = cur.rowcount
        result = cur.fetchone()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
            customer = Customer()
            customer.setCustomerID(result[0])
            customer.setPasswordHash(result[1])
            customer.setRegisterDatetime(result[2])
            customer.setEmailAddress(result[3])
            customer.setPreviousSignInDatetime(result[4])
            customer.setCurrentSignInDatetime(result[5])
            customer.setName(result[6])

            return customer
        else:
            raise LookupError("Customer record does not exist")

    def readCustomerByCustomerID(self, customerID):
        query = "SELECT * FROM Customer " \
                "WHERE CustomerID = %s"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(query, customerID)
        rowCount = cur.rowcount
        result = cur.fetchone()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
            customer = Customer()
            customer.setCustomerID(result[0])
            customer.setPasswordHash(result[1])
            customer.setRegisterDatetime(result[2])
            customer.setEmailAddress(result[3])
            customer.setPreviousSignInDatetime(result[4])
            customer.setCurrentSignInDatetime(result[5])
            customer.setName(result[6])

            return customer
        else:
            raise LookupError("Customer record does not exist")

    def updateCustomerPassword(self, customerObj):
        query = "UPDATE Customer SET PasswordHash = %s " \
                "WHERE CustomerID = %s"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(query,
                    (customerObj.getPasswordHash(),
                     customerObj.getCustomerID()))

        cur.close()
        con.commit()
        con.close()

    def updateCustomerEmailAddress(self, customerObj):
        query = "UPDATE Customer SET EmailAddress = %s " \
                "WHERE CustomerID = %s"

        con = self.mysql.connect()
        cur = con.cursor()

        cur.execute(query,
                    (customerObj.getEmailAddress(),
                     customerObj.getCustomerID()))

        cur.close()
        con.commit()
        con.close()

    def updateCustomerSignInDatetimes(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        updateQuery = "UPDATE Customer SET PreviousSignInDatetime = %s, " \
                      "CurrentSignInDatetime = %s " \
                      "WHERE CustomerID = %s"

        cur.execute(updateQuery,
                    (customerObj.getPreviousSignInDatetime(),
                     customerObj.getCurrentSignInDatetime(),
                     customerObj.getCustomerID()))

        cur.close()
        con.commit()
        con.close()

    def testDropTables(self):
        # Just for unit testing
        con = self.mysql.connect()
        cur = con.cursor()
        dropQuery = "DROP TABLE Customer"
        cur.execute(dropQuery)
        cur.close()
        con.commit()
        con.close()
