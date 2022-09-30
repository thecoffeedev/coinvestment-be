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
        self.createTables()
        self.insertDayZeroData()

        c = Customer()
        c.setCustomerID("1WNJKpBpYfWwKIlvbaz0")
        c.setCurrentSignInDatetime(12345)
        c.setPreviousSignInDatetime(67890)
        self.updateCustomerSignInDatetimes(c)


    def createTables(self):
        createTableQuery = "CREATE TABLE IF NOT EXISTS Customer (" \
                            "CustomerID VARCHAR(20), " \
                            "PasswordHash VARCHAR(60), " \
                            "RegisterDatetime INT, " \
                            "EmailAddress VARCHAR(256), " \
                            "PreviousSignInDatetime INT, " \
                            "CurrentSignInDatetime INT, " \
                            "Name VARCHAR(256)" \
                            ")"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createTableQuery)
        cur.close()
        con.close()

    def insertDayZeroData(self):
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

        con = self.mysql.connect()
        cur = con.cursor()

        # If the table exists and is empty, insert the customer models
        cur.execute("SELECT EXISTS (SELECT * FROM Customer)")

        if not cur.fetchone()[0]:
            self.insertCustomer(customerOne)
            self.insertCustomer(customerTwo)

        cur.close()
        con.commit()
        con.close()

    def insertCustomer(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        insertQuery = "INSERT INTO Customer (" \
                "CustomerID, PasswordHash, RegisterDatetime, EmailAddress, PreviousSignInDatetime, " \
                "CurrentSignInDatetime, Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        cur.execute(insertQuery, (customerObj.getCustomerID(), customerObj.getPasswordHash(),
                                  customerObj.getRegisterDatetime(), customerObj.getEmailAddress(),
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

        return customer

    def updateCustomerPassword(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("UPDATE Customer SET PasswordHash = %s "
                    "WHERE CustomerID = %s",
                    (customerObj.getPasswordHash(),
                     customerObj.getCustomerID()))

        cur.close()
        con.commit()
        con.close()

    def updateCustomerSignInDatetimes(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("UPDATE Customer SET PreviousSignInDatetime = %s, "
                    "CurrentSignInDatetime = %s "
                    "WHERE CustomerID = %s",
                    (customerObj.getPreviousSignInDatetime(),
                     customerObj.getCurrentSignInDatetime(),
                    customerObj.getCustomerID()))

        result = cur.fetchone()
        print(result)
        cur.close()
        con.commit()
        con.close()




"""
        cur.execute('INSERT INTO user (username, email, password)VALUES( %s,  %s, %s)',
                        (username, email, password))

        con.commit()

"""

