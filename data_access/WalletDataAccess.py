from flaskext.mysql import MySQL
from models.Wallet import Wallet
from models.Utility import Utility
from models.WalletTransactionHistory import WalletTransactionHistory
from decouple import config


class WalletDataAccess:

    def __init__(self, app):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = config('DB_USER')
        app.config['MYSQL_DATABASE_PASSWORD'] = config('DB_PASSWORD')
        app.config['MYSQL_DATABASE_DB'] = config('DB_NAME')
        app.config['MYSQL_DATABASE_HOST'] = config('DB_HOST')
        self.mysql.init_app(app)
        # self.mysqlDB = MySQL()
        # self.readWalletFromWalletAddress("UazgXbwu2tloBcajCPb8")
        # self.readWalletFromWalletAddress("UazgXbwu2tloBcajCPb")
        # self.readWalletFromCustomerID("Debo32tKqJBeZwHHgkvx")

    def createTables(self):
        # Create the table if it does not exist
        createQuery = "CREATE TABLE IF NOT EXISTS AvailableCryptocurrency(" \
                      "cryptocurrencyCode VARCHAR(10) NOT NULL PRIMARY KEY, " \
                      "name VARCHAR(20) NOT NULL" \
                      ")"
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createQuery)
        cur.close()
        con.commit()
        con.close()

    def generateDayZeroData(self):
        # Create the table if it does not exist
        createQuery = "CREATE TABLE IF NOT EXISTS AvailableCryptocurrency(" \
                "cryptocurrencyCode VARCHAR(10) NOT NULL PRIMARY KEY, " \
                "name VARCHAR(20) NOT NULL" \
                ")"
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createQuery)

        # If the table exists and is empty, insert the values
        cur.execute("SELECT EXISTS (SELECT * FROM AvailableCryptocurrency)")

        if not cur.fetchone()[0]:
            currencyList = [('btc', 'Bitcoin'), ('eth', 'Ethereum'), ('usdt', 'Tether'), ('usdc', 'USD Coin'),
                            ('bnb', 'BNB'), ('xrp', 'XRP'), ('busd', 'Binance USD'), ('ada', 'Cardano'),
                            ('sol', 'Solana'), ('doge', 'Dogecoin'), ('dot', 'Polkadot'), ('shib', 'Shiba Inu'),
                            ('dai', 'Dai'), ('steth', 'Lido Staked Ether'), ('matic', 'Polygon'), ('trx', 'TRON'),
                            ('avax', 'Avalanche'), ('uni', 'Uniswap'), ('wbtc', 'Wrapped Bitcoin'),
                            ('leo', 'LEO Token'), ('link', 'Chainlink'), ('okb', 'OKB'), ('etc', 'Ethereum Classic'),
                            ('atom', 'Cosmos Hub'), ('ltc', 'Litecoin'), ('ftt', 'FTX'), ('cro', 'Cronos'),
                            ('near', 'NEAR Protocol'), ('xlm', 'Stellar'), ('xmr', 'Monero'), ('algo', 'Algorand'),
                            ('bch', 'Bitcoin Cash'), ('lunc', 'Terra Luna Classic'), ('qnt', 'Quant'), ('flow', 'Flow'),
                            ('fil', 'Filecoin'), ('ape', 'ApeCoin'), ('vet', 'VeChain'), ('icp', 'Internet Computer'),
                            ('xcn', 'Chain'), ('hbar', 'Hedera'), ('frax', 'Frax'), ('chz', 'Chiliz'), ('xtz', 'Tezos'),
                            ('mana', 'Decentraland'), ('sand', 'The Sandbox'), ('eos', 'EOS'), ('axs', 'Axie Infinity'),
                            ('theta', 'Theta Network'), ('egld', 'Elrond')]

            insertQuery = "INSERT INTO AvailableCryptocurrency (cryptocurrencyCode, name) VALUES (%s, %s)"
            cur.executemany(insertQuery, currencyList)
            cur.close()
            con.commit()

        # Check if the table exists
        #checkTableExistsQuery = "SELECT * FROM information_schema.tables WHERE table_name = 'AvailableCryptocurrency'"
        #cur.execute(checkTableExistsQuery)

    def createWallet(self):
        print("createWallet entry")
        createTableQuery = "CREATE TABLE IF NOT EXISTS Wallet (" \
                           "WalletAddress VARCHAR(20) NOT NULL PRIMARY KEY, " \
                           "CustomerID VARCHAR(20), " \
                           "InitialBalance FLOAT(53), " \
                           "CurrentBalance FLOAT(53), " \
                           "CryptocurrencyCode VARCHAR(10), " \
                           "HoldingPeriod INT(5) " \
                           ")"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createTableQuery)
        cur.close()
        con.close()
        print("createWallet exit")

    def createWalletTransactionHistory(self):
        print("createWallet entry")
        createTableQuery = "CREATE TABLE IF NOT EXISTS WalletTransactionHistory (" \
                           "TransactionID VARCHAR(20) NOT NULL PRIMARY KEY, " \
                           "WalletAddress VARCHAR(20), " \
                           "UnitsSold FLOAT(35), " \
                           "TransactionDatetime INT, " \
                           "ChargeApplied FLOAT(53), " \
                           "Amount FLOAT(53), " \
                           "Action VARCHAR(10), " \
                           "CardNumber VARCHAR(20), " \
                           "Expiry VARCHAR(20), " \
                           "InitialRate FLOAT(53)" \
                           ")"

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createTableQuery)
        cur.close()
        con.close()
        print("createWallet exit")


    def insertDayZeroWalletData(self):
        print("insertDayZeroWalletData entry")
        con = self.mysql.connect()
        cur = con.cursor()

        # If the table exists and is empty, insert the customer models
        cur.execute("select exists (SELECT * FROM Wallet)")
        # result = cur.fetchall()
        # print("result ", result)
        # print("result one ", cur.fetchone()[0])

        if not cur.fetchone()[0]:
            print("result not exists")
            walletOne = Wallet()
            walletOne.setCustomerID("1WNJKpBpYfWwKIlvbaz0")
            walletOne.setWalletAddress(Utility.generateRandomID())
            print("wallet address ", walletOne.getWalletAddress())
            walletOne.setInitialBalance(8432.2871)
            walletOne.setCurrentBalance(8432.2871)
            walletOne.setCryptocurrencyCode('btc')
            walletOne.setHoldingPeriod(24)
            self.insertWallet(walletOne)

            walletOne = Wallet()
            walletOne.setCustomerID("Debo32tKqJBeZwHHgkvx")
            walletOne.setWalletAddress(Utility.generateRandomID())
            print("wallet address ", walletOne.getWalletAddress())
            walletOne.setInitialBalance(2731.3329)
            walletOne.setCurrentBalance(2731.3329)
            walletOne.setCryptocurrencyCode('trx')
            walletOne.setHoldingPeriod(10)
            self.insertWallet(walletOne)
        print("insertDayZeroWalletData exit")


    def insertWallet(self, walletObj):
        print("insertWallet entry")
        print("walletObj :", walletObj.__dict__)
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO Wallet (WalletAddress, CustomerID, InitialBalance, CurrentBalance, " \
                    "CryptocurrencyCode, HoldingPeriod) VALUES(%s, %s, %s, %s,  %s, %s)",
                    (walletObj.getWalletAddress(), walletObj.getCustomerID(), walletObj.getInitialBalance(),
                    walletObj.getCurrentBalance(), walletObj.getCryptocurrencyCode(), walletObj.getHoldingPeriod()))
        cur.close()
        con.commit()
        con.close()
        print("Insert successful.")
        print("insertWallet exit")

    def insertWalletTransactionHistory(self, walletTransactionObj):
        print("insertWalletTransactionHistory entry")
        print("walletTransactionObj :", walletTransactionObj.__dict__)
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO WalletTransactionHistory" \
                    " (TransactionID, TransactionDatetime, ChargeApplied, Amount," \
                    " Action, CardNumber, Expiry, WalletAddress, UnitsSold, InitialRate) " \
                    " VALUES(%s, %s, %s, %s,  %s, %s, %s, %s, %s, %s)",
                    (walletTransactionObj.getTransactionID(),
                    walletTransactionObj.getTransactionDatetime(),
                    walletTransactionObj.getChargeApplied(),
                    walletTransactionObj.getAmount(),
                    walletTransactionObj.getAction(),
                    walletTransactionObj.getCardNumber(),
                    walletTransactionObj.getExpiry(),
                    walletTransactionObj.getWalletAddress(),
                    walletTransactionObj.getUnitsSold(),
                    walletTransactionObj.getInitialRate()))
        cur.close()
        con.commit()
        con.close()
        print("Insert successful.")
        print("insertWalletTransactionHistory exit")


    def readWalletFromWalletAddress(self, walletAddress):
        print("readWalletFromWalletAddress entry")
        print("walletAddress : ", walletAddress)
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Wallet where WalletAddress = %s", walletAddress)
        rowCount = cur.rowcount
        wallet = cur.fetchone()

        cur.close()
        con.commit()
        con.close()

        print(wallet)
        print(rowCount)
        if rowCount:
            walletOne = Wallet()
            walletOne.setCustomerID(wallet[1])
            walletOne.setWalletAddress(wallet[0])
            walletOne.setInitialBalance(wallet[2])
            walletOne.setCurrentBalance(wallet[3])
            walletOne.setCryptocurrencyCode(wallet[4])
            walletOne.setHoldingPeriod(wallet[5])
            print(" walletOne : ", walletOne.__dict__)
            print("readWalletFromWalletAddress exit")
            return walletOne
        else:
            raise LookupError("No wallet exists")

    def readWalletsFromCustomerID(self, customerID):
        print("readWalletsFromCustomerID entry")
        print("customerID : ", customerID)

        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Wallet where customerID = %s", customerID)
        rowCount = cur.rowcount
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
            walletsList = list()
            for wallet in result:
                print(wallet)
                walletOne = Wallet()
                walletOne.setCustomerID(wallet[1])
                walletOne.setWalletAddress(wallet[0])
                walletOne.setInitialBalance(wallet[2])
                walletOne.setCurrentBalance(wallet[3])
                walletOne.setCryptocurrencyCode(wallet[4])
                walletOne.setHoldingPeriod(wallet[5])
                print(walletOne.__dict__)
                walletsList.append(walletOne)
            print(walletsList)
            print("readWalletsFromCustomerID exit")
            return walletsList
        else:
            raise LookupError("No wallet exists")

    def readWalletTransactionsFromWalletAddress(self, walletAddress):
        print("readWalletTransactionsFromWalletAddress entry")
        print("walletAddress : ", walletAddress)
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM WalletTransactionHistory where WalletAddress = '"+walletAddress+"'")
        rowCount = cur.rowcount
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
            walletTransactionsList = list()
            for walletTransaction in result:
                print(walletTransaction)
                walletTransactionObj = WalletTransactionHistory()
                walletTransactionObj.setTransactionID(walletTransaction[0])
                walletTransactionObj.setWalletAddress(walletTransaction[1])
                walletTransactionObj.setUnitsSold(walletTransaction[2])
                walletTransactionObj.setTransactionDatetime(walletTransaction[3])
                walletTransactionObj.setChargeApplied(walletTransaction[4])
                walletTransactionObj.setAmount(walletTransaction[5])
                walletTransactionObj.setAction(walletTransaction[6])
                walletTransactionObj.setCardNumber(walletTransaction[7])
                walletTransactionObj.setExpiry(walletTransaction[8])
                walletTransactionObj.setInitialRate(walletTransaction[9])
                print(" walletTransactionObj :", walletTransactionObj.__dict__)
                walletTransactionsList.append(walletTransactionObj)

            print("walletTransactionsList : ", walletTransactionsList)
            print("readWalletTransactionsFromWalletAddress exit")
            return walletTransactionsList
        else:
            raise LookupError("No wallet transaction exists")

    def readPurchaseWalletTransactionFromWalletAddress(self, walletAddress):
        print("readWalletTransactionsFromWalletAddress entry")
        print("walletAddress : ", walletAddress)
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM WalletTransactionHistory where Action='BUY' and WalletAddress = '"+walletAddress+"'")
        rowCount = cur.rowcount
        walletTransaction = cur.fetchone()
        cur.close()
        con.commit()
        con.close()
        print(rowCount)
        if rowCount:
            print(walletTransaction)
            walletTransactionObj = WalletTransactionHistory()
            walletTransactionObj.setTransactionID(walletTransaction[0])
            walletTransactionObj.setWalletAddress(walletTransaction[1])
            walletTransactionObj.setUnitsSold(walletTransaction[2])
            walletTransactionObj.setTransactionDatetime(walletTransaction[3])
            walletTransactionObj.setChargeApplied(walletTransaction[4])
            walletTransactionObj.setAmount(walletTransaction[5])
            walletTransactionObj.setAction(walletTransaction[6])
            walletTransactionObj.setCardNumber(walletTransaction[7])
            walletTransactionObj.setExpiry(walletTransaction[8])
            walletTransactionObj.setInitialRate(walletTransaction[9])
            print(" walletTransactionObj :", walletTransactionObj.__dict__)
            print("readWalletTransactionsFromWalletAddress exit")
            return walletTransactionObj
        else:
            raise LookupError("No wallet transaction record exists")


    def updateWalletCurrentBalance(self, walletObj):
        print("updateWalletCurrentBalance entry")
        print("walletObj : ", walletObj.__dict__)
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("UPDATE Wallet set CurrentBalance = %s where WalletAddress = %s",
                    (walletObj.getCurrentBalance(), walletObj.getWalletAddress()))
        cur.close()
        con.commit()
        con.close()
        print("Update Successful")
        print("updateWalletCurrentBalance exit")