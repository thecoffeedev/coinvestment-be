from flaskext.mysql import MySQL
from decouple import config


class WalletDataAccess:

    def __init__(self, app):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
        app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
        self.mysql.init_app(app)

        self.mysqlDB = MySQL()


    def createWallet(self):
        print("in wallet data access")
        # # self.mysql = MySQL()
        # # Creating a connection cursor
        # cursor = self.mysql.connect().cursor()
        #
        # # Executing SQL Statements
        # query = "CREATE TABLE test3(id VARCHAR(20), name VARCHAR(20))"
        # cursor.execute(query)
        #
        # query = "INSERT INTO test3('1', 'Nikita')"
        # cursor.execute(query)
        #
        # # Saving the Actions performed on the DB
        # self.mysql.connect().commit()
        #
        # # Closing the cursor
        # cursor.close()
        # print(" Table created successfully ")

        conn = self.mysqlDB.connect(MYSQL_DATABASE_USER='root', MYSQL_DATABASE_PASSWORD='', MYSQL_DATABASE_HOST='127.0.0.1')
        cursorDB = conn.cursor()
        sql = "CREATE database MYDATABASE"
        cursor.execute(sql)
        conn.close()
        print(" DB created successfully ")