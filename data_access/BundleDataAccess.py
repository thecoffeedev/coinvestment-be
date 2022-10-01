from flaskext.mysql import MySQL
from decouple import config


class BundleDataAccess:

    def __init__(self, app):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
        app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
        self.mysql.init_app(app)

        # self.mysqlDB = MySQL()

    def insertDayZeroData(self):
        # Create the table if it does not exist
        createQuery = "CREATE TABLE IF NOT EXISTS AvailableBundle(" \
                "bundleID VARCHAR(10) NOT NULL, " \
                "cryptocurrencyCode VARCHAR(10) NOT NULL, " \
                "percentage INT NOT NULL, " \
                "holdingPeriod INT NOT NULL" \
                      ")"
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createQuery)

        # If the table exists and is empty, insert the values
        cur.execute("SELECT EXISTS (SELECT * FROM AvailableBundle)")

        if not cur.fetchone()[0]:
            bundleList = [(1, "btc", 50, 6), (1, "eth", 50, 6),
                            (2, 'bch', 25, 12), (2, 'eth', 15, 12), (2, 'xrp', 15, 12), (2, 'ltc', 25, 12), (2, 'xmr', 20, 12),
                            (3, 'doge', 20, 12), (3, 'shib', 20, 12), (3, 'etc', 30, 12), (3, 'ape', 30, 12),
                            (4, 'link', 20, 12), (4, 'mana', 20, 12), (4, 'qnt', 20, 12), (4, 'wbtc', 20, 12), (4, 'usdc', 20, 12),
                            (5, 'dai', 20, 12), (5, 'bnb', 20, 12), (5, 'sol', 20, 12),
                            (6, 'algo', 20, 18), (6, 'busd', 20, 18), (6, 'flow', 20, 18), (6, 'fil', 20, 18), (6, 'dot', 20, 18)
                            ]

            insertQuery = "INSERT INTO AvailableBundle VALUES (%s, %s, %s, %s)"
            cur.executemany(insertQuery, bundleList)
            cur.close()
            con.commit()

        # Check if the table exists
        #checkTableExistsQuery = "SELECT * FROM information_schema.tables WHERE table_name = 'AvailableBundle'"
        #cur.execute(checkTableExistsQuery)


"""
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
        """