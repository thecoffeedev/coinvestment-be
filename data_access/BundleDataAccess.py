from flaskext.mysql import MySQL
from decouple import config
from models.Bundle import Bundle
from models.BundleTransactionHistory import BundleTransactionHistory


class BundleDataAccess:

    def __init__(self, app):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
        app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
        self.mysql.init_app(app)

    def createTables(self):
        con = self.mysql.connect()
        cur = con.cursor()

        # Create the table if it does not exist
        createQuery = "CREATE TABLE IF NOT EXISTS AvailableBundle(" \
                      "BundleID VARCHAR(10) NOT NULL, " \
                      "CryptocurrencyCode VARCHAR(50) NOT NULL, " \
                      "Percentage INT NOT NULL, " \
                      "HoldingPeriod INT NOT NULL" \
                      ") DEFAULT COLLATE=utf8_bin"

        cur.execute(createQuery)

        createQuery = "CREATE TABLE IF NOT EXISTS Bundle(" \
                      "BundleAddress VARCHAR(20) NOT NULL, " \
                      "BundleID VARCHAR(10) NOT NULL, " \
                      "CustomerID VARCHAR(20) NOT NULL, " \
                      "HoldingPeriod INT NOT NULL," \
                      "PurchaseDatetime INT NOT NULL, " \
                      "Status VARCHAR(20) NOT NULL " \
                      ") DEFAULT COLLATE=utf8_bin"

        cur.execute(createQuery)

        createQuery = "CREATE TABLE IF NOT EXISTS BundleTransactionHistory(" \
                      "TransactionID VARCHAR(20) NOT NULL, " \
                      "BundleAddress VARCHAR(20) NOT NULL, " \
                      "Action VARCHAR(10), " \
                      "TransactionDatetime INT, " \
                      "ChargeApplied FLOAT(53), " \
                      "Amount FLOAT(53), " \
                      "CardNumber VARCHAR(20), " \
                      "Expiry VARCHAR(20), " \
                      "InitialRate FLOAT(53)" \
                      ") DEFAULT COLLATE=utf8_bin"

        cur.execute(createQuery)

        cur.close()
        con.close()

    def insertDayZeroData(self):

        con = self.mysql.connect()
        cur = con.cursor()

        # If the table exists and is empty, insert the values
        cur.execute("SELECT EXISTS (SELECT * FROM AvailableBundle)")

        if not cur.fetchone()[0]:
            bundleList = [(1, "bitcoin", 50, 6), (1, "ethereum", 50, 6),
                        (2, 'bitcoin-cash', 25, 6), (2, 'tether', 15, 6), (2, 'ripple', 15, 6), (2, 'litecoin', 25, 6), (2, 'monero', 20, 6),
                        (3, 'dogecoin', 20, 12), (3, 'shiba-inu', 20, 12), (3, 'ethereum-classic', 30, 12), (3, 'apecoin', 30, 12),
                        (4, 'chainlink', 20, 12), (4, 'decentraland', 20, 12), (4, 'quant-network', 20, 12), (4, 'wrapped-bitcoin', 20, 12), (4, 'usd-coin', 20, 12),
                        (5, 'dai', 20, 18), (5, 'binancecoin', 20, 18), (5, 'solana', 20, 18),
                        (6, 'algorand', 20, 18), (6, 'binance-usd', 20, 18), (6, 'flow', 20, 18), (6, 'filecoin', 20, 18), (6, 'polkadot', 20, 18)
                        ]

            insertQuery = "INSERT INTO AvailableBundle VALUES (%s, %s, %s, %s)"
            cur.executemany(insertQuery, bundleList)

        cur.execute("SELECT EXISTS (SELECT * FROM Bundle)")
        if not cur.fetchone()[0]:
            bundleOne = Bundle()
            bundleOne.setBundleAddress("kv908kmPkhFImJrZ4R1i")
            bundleOne.setBundleID("1")
            bundleOne.setCustomerID("1WNJKpBpYfWwKIlvbaz0")
            bundleOne.setHoldingPeriod(12)
            bundleOne.setPurchaseDatetime(1664645692)
            bundleOne.setStatus("ACTIVE")

            bundleTwo = Bundle()
            bundleTwo.setBundleAddress("CiHp30zstnE1ufu7M8P5")
            bundleTwo.setBundleID("2")
            bundleTwo.setCustomerID("1WNJKpBpYfWwKIlvbaz0")
            bundleTwo.setHoldingPeriod(18)
            bundleTwo.setPurchaseDatetime(1664645764)
            bundleTwo.setStatus("ACTIVE")

            bundleThree = Bundle()
            bundleThree.setBundleAddress("YRoIXn82skSGBhl9zJyg")
            bundleThree.setBundleID("4")
            bundleThree.setCustomerID("Debo32tKqJBeZwHHgkvx")
            bundleThree.setHoldingPeriod(18)
            bundleThree.setPurchaseDatetime(1664645865)
            bundleThree.setStatus("ACTIVE")

            self.insertBundle(bundleOne)
            self.insertBundle(bundleTwo)
            self.insertBundle(bundleThree)

        cur.execute("SELECT EXISTS (SELECT * FROM BundleTransactionHistory)")
        if not cur.fetchone()[0]:
            # Bundle transaction models and insertion goes here
            bundleTransactionObj = BundleTransactionHistory()
            bundleTransactionObj.setTransactionID("tq5BBZAlv1P3zH3nIe1j")
            bundleTransactionObj.setBundleAddress("kv908kmPkhFImJrZ4R1i")
            bundleTransactionObj.setAction("BUY")
            bundleTransactionObj.setTransactionDatetime(1664645692)
            bundleTransactionObj.setChargeApplied(0.00)
            bundleTransactionObj.setAmount(5000.00)
            bundleTransactionObj.setCardNumber("4921852004294232")
            bundleTransactionObj.setExpiry("05/24")
            bundleTransactionObj.setInitialRate(19383.26)

            bundleTransactionObjTwo = BundleTransactionHistory()
            bundleTransactionObjTwo.setTransactionID("SB1UvWj6DSw2819Tk71B")
            bundleTransactionObjTwo.setBundleAddress("CiHp30zstnE1ufu7M8P5")
            bundleTransactionObjTwo.setAction("BUY")
            bundleTransactionObjTwo.setTransactionDatetime(1664645764)
            bundleTransactionObjTwo.setChargeApplied(0.00)
            bundleTransactionObjTwo.setAmount(1000.00)
            bundleTransactionObjTwo.setCardNumber("4921852004294232")
            bundleTransactionObjTwo.setExpiry("05/24")
            bundleTransactionObjTwo.setInitialRate(1369.57)

            bundleTransactionObjThree = BundleTransactionHistory()
            bundleTransactionObjThree.setTransactionID("OVIYf5sJqzosP8dBOAXD")
            bundleTransactionObjThree.setBundleAddress("YRoIXn82skSGBhl9zJyg")
            bundleTransactionObjThree.setAction("BUY")
            bundleTransactionObjThree.setTransactionDatetime(1664645865)
            bundleTransactionObjThree.setChargeApplied(0.00)
            bundleTransactionObjThree.setAmount(500.00)
            bundleTransactionObjThree.setCardNumber("4857037529348105")
            bundleTransactionObjThree.setExpiry("03/23")
            bundleTransactionObjThree.setInitialRate(735.23)

            self.insertBundleTransactionHistory(bundleTransactionObj)
            self.insertBundleTransactionHistory(bundleTransactionObjTwo)
            self.insertBundleTransactionHistory(bundleTransactionObjThree)

        cur.close()
        con.commit()

        # Check if the table exists
        #checkTableExistsQuery = "SELECT * FROM information_schema.tables WHERE table_name = 'AvailableBundle'"
        #cur.execute(checkTableExistsQuery)

    def insertBundle(self, bundleObj):
        con = self.mysql.connect()
        cur = con.cursor()

        query = "INSERT INTO Bundle (BundleAddress, BundleID, CustomerID, " \
                "HoldingPeriod, PurchaseDatetime, Status) " \
                "VALUES(%s, %s, %s, %s, %s, %s)"

        cur.execute(query, (bundleObj.getBundleAddress(), bundleObj.getBundleID(),
                            bundleObj.getCustomerID(), bundleObj.getHoldingPeriod(),
                            bundleObj.getPurchaseDatetime(), bundleObj.getStatus()))

        cur.close()
        con.commit()
        con.close()

    def insertBundleTransactionHistory(self, bundleTransactionObj):
        con = self.mysql.connect()
        cur = con.cursor()

        query = "INSERT INTO BundleTransactionHistory (" \
                "TransactionID, BundleAddress, Action, " \
                "TransactionDateTime, ChargeApplied, " \
                "Amount, CardNumber, Expiry, InitialRate " \
                ") " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cur.execute(query,
                    (bundleTransactionObj.getTransactionID(),
                     bundleTransactionObj.getBundleAddress(),
                     bundleTransactionObj.getAction(),
                     bundleTransactionObj.getTransactionDatetime(),
                     bundleTransactionObj.getChargeApplied(),
                     bundleTransactionObj.getAmount(),
                     bundleTransactionObj.getCardNumber(),
                     bundleTransactionObj.getExpiry(),
                     bundleTransactionObj.getInitialRate()
                     ))

        cur.close()
        con.commit()
        con.close()

    def readBundleByBundleAddress(self, bundleAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Bundle WHERE BundleAddress = %s", bundleAddress)
        result = cur.fetchone()
        cur.close()
        con.commit()
        con.close()

        if result:
            bundle = Bundle()
            bundle.setBundleAddress(result[0])
            bundle.setBundleID(result[1])
            bundle.setCustomerID(result[2])
            bundle.setHoldingPeriod(result[3])
            bundle.setPurchaseDatetime(result[4])
            bundle.setStatus(result[5])

            return bundle
        else:
            raise LookupError("No bundle found with address provided")

    def readBundlesByCustomerID(self, customerID):
        con = self.mysql.connect()
        cur = con.cursor()
        query = "SELECT * FROM Bundle WHERE CustomerID = %s"
        cur.execute(query, customerID)
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        bundles = []

        if result:
            for bundle in result:
                bundleObj = Bundle()
                bundleObj.setBundleAddress(bundle[0])
                bundleObj.setBundleID(bundle[1])
                bundleObj.setCustomerID(bundle[2])
                bundleObj.setHoldingPeriod(bundle[3])
                bundleObj.setPurchaseDatetime(bundle[4])
                bundleObj.setStatus(bundle[5])
                bundles.append(bundleObj)

            return bundles
        else:
            raise LookupError("No bundle found with customer ID provided")

    def readBundleTransactionsByBundleAddress(self, bundleAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        query = "SELECT * FROM BundleTransactionHistory " \
                "WHERE BundleAddress = %s order by TransactionDatetime desc "

        cur.execute(query, bundleAddress)
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        if result:
            bundleTransactions = []
            for bundleTransaction in result:
                bundleTransactionObj = BundleTransactionHistory()
                bundleTransactionObj.setTransactionID(bundleTransaction[0])
                bundleTransactionObj.setBundleAddress(bundleTransaction[1])
                bundleTransactionObj.setAction(bundleTransaction[2])
                bundleTransactionObj.setTransactionDatetime(bundleTransaction[3])
                bundleTransactionObj.setChargeApplied(bundleTransaction[4])
                bundleTransactionObj.setAmount(bundleTransaction[5])
                bundleTransactionObj.setCardNumber(bundleTransaction[6])
                bundleTransactionObj.setExpiry(bundleTransaction[7])
                bundleTransactionObj.setInitialRate(bundleTransaction[8])

                bundleTransactions.append(bundleTransactionObj)

            return bundleTransactions
        else:
            raise LookupError("No bundle transactions found for the bundle address proved")

    def updateBundleStatus(self, bundleObj):
        con = self.mysql.connect()
        cur = con.cursor()
        updateQuery = "UPDATE Bundle set Status = %s " \
                      "WHERE BundleAddress = %s"

        cur.execute(updateQuery,
                    (bundleObj.getStatus(),
                     bundleObj.getBundleAddress()))

        cur.close()
        con.commit()
        con.close()

    
    def readPurchaseBundleTransactionFromBundleAddress(self, bundleAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM BundleTransactionHistory where Action='BUY' and BundleAddress = '"+bundleAddress+"'")
        rowCount = cur.rowcount
        bundleTransaction = cur.fetchone()
        cur.close()
        con.commit()
        con.close()
        if rowCount:
            bundleTransactionObj = BundleTransactionHistory()
            bundleTransactionObj.setTransactionID(bundleTransaction[0])
            bundleTransactionObj.setBundleAddress(bundleTransaction[1])
            bundleTransactionObj.setAction(bundleTransaction[2])
            bundleTransactionObj.setTransactionDatetime(bundleTransaction[3])
            bundleTransactionObj.setChargeApplied(bundleTransaction[4])
            bundleTransactionObj.setAmount(bundleTransaction[5])
            bundleTransactionObj.setCardNumber(bundleTransaction[6])
            bundleTransactionObj.setExpiry(bundleTransaction[7])
            bundleTransactionObj.setInitialRate(bundleTransaction[8])
            return bundleTransactionObj
        else:
            raise LookupError("No bundle transaction record exists")

    def readAllAvailableBundles(self):
        con = self.mysql.connect()
        cur = con.cursor()
        query = "SELECT a.*, b.name FROM AvailableBundle a, AvailableCryptocurrency b where a.CryptocurrencyCode = b.CryptocurrencyCode "
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()
        return result

    def testDropTables(self):
        # Just for unit testing
        con = self.mysql.connect()
        cur = con.cursor()
        dropQuery = "DROP TABLE Bundle"
        cur.execute(dropQuery)
        dropQuery = "DROP TABLE BundleTransactionHistory"
        cur.execute(dropQuery)
        cur.close()
        con.commit()
        con.close()
