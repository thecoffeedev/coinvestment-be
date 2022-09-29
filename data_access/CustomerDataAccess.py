from flaskext.mysql import MySQL
from decouple import config  # for environment variables


class CustomerDataAccess:

    def __init__(self, app):
        self.mysql = MySQL()
        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
        app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
        self.mysql.init_app(app)

    @classmethod
    def createTables(cls):
        sql = "CREATE TABLE IF NOT EXISTS Customer (" \
              "CustomerID VARCHAR(20)," \
              "PasswordHash VARCHAR(60)," \
              "RegisterDatetime FLOAT(53)" \
              "EmailAddress VARCHAR(256)" \
              "PreviousSignInDatetime FLOAT(53)" \
              "CurrentSignInDatetime FLOAT(53)" \
              "Name VARCHAR(256)"



    def customerExists(self, emailAddress):
        connection = self.mysql.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Customer WHERE emailAddress = '%s'", emailAddress)
        connection.commit()




        """cur.execute('INSERT INTO user (username, email, password)VALUES( %s,  %s, %s)',
                        (username, email, password))

            con.commit()
            msg = "You have signed up today (UK Time)"
        """

