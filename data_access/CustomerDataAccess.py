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
        createTableQuery =  "CREATE TABLE IF NOT EXISTS Customer (" \
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

    def fetchCustomer(self, customerObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Customer WHERE emailAddress = %s", customerObj.getEmailAddress())
        entry = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        customerObj.setCustomerID(entry.customerID)





"""cur.execute('INSERT INTO user (username, email, password)VALUES( %s,  %s, %s)',
                        (username, email, password))

            con.commit()
            msg = "You have signed up today (UK Time)"
"""

