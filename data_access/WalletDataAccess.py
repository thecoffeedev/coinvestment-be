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

    def createTables(self):
        # Create the table if it does not exist
        createAvailableTableQuery = \
            "CREATE TABLE IF NOT EXISTS AvailableCryptocurrency(" \
            "cryptocurrencyCode VARCHAR(10) NOT NULL PRIMARY KEY, " \
            "name VARCHAR(20) NOT NULL" \
            ")"

        createWalletTableQuery = \
            "CREATE TABLE IF NOT EXISTS Wallet (" \
            "WalletAddress VARCHAR(20) NOT NULL PRIMARY KEY, " \
            "CustomerID VARCHAR(20), " \
            "InitialBalance FLOAT(53), " \
            "CurrentBalance FLOAT(53), " \
            "CryptocurrencyCode VARCHAR(10), " \
            "HoldingPeriod INT(5) " \
            ")"

        createWallletTransactionTableQuery = \
            "CREATE TABLE IF NOT EXISTS WalletTransactionHistory (" \
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
        cur.execute(createAvailableTableQuery)
        cur.execute(createWalletTableQuery)
        cur.execute(createWallletTransactionTableQuery)

        cur.close()
        con.commit()
        con.close()

    def insertDayZeroData(self):
        con = self.mysql.connect()
        cur = con.cursor()

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

        cur.execute("select exists (SELECT * FROM Wallet)")

        if not cur.fetchone()[0]:
            walletZero = Wallet()
            walletZero.setCustomerID("1WNJKpBpYfWwKIlvbaz0")
            walletZero.setWalletAddress("jNrxO4OyXgdqum0wj2LV")
            walletZero.setInitialBalance(2.2632)
            walletZero.setCurrentBalance(2.2632)
            walletZero.setCryptocurrencyCode('btc')
            walletZero.setHoldingPeriod(24)
            self.insertWallet(walletZero)

            walletOne = Wallet()
            walletOne.setCustomerID("Debo32tKqJBeZwHHgkvx")
            walletOne.setWalletAddress("hrD3IxwVUWloVP0nrIct")
            walletOne.setInitialBalance(18248.1751)
            walletOne.setCurrentBalance(18248.1751)
            walletOne.setCryptocurrencyCode('trx')
            walletOne.setHoldingPeriod(12)
            self.insertWallet(walletOne)

        cur.execute("select exists (SELECT * FROM Wallet)")
        if not cur.fetchone()[0]:
            walletTransZero = WalletTransactionHistory()
            walletTransZero.setTransactionID("nmagkxkfXvN9WgMe9wvt")
            walletTransZero.setTransactionDatetime(1664971119)
            walletTransZero.setChargeApplied(0.0)
            walletTransZero.setAmount(40000.00)
            walletTransZero.setAction("BUY")
            walletTransZero.setCardNumber("4921934757374347")
            walletTransZero.setExpiry("07/25")
            walletTransZero.setInitialRate(17617.53)
            walletTransZero.setWalletAddress("jNrxO4OyXgdqum0wj2LV")
            walletTransZero.setUnitsSold(0.0)

            walletTransOne = WalletTransactionHistory()
            walletTransOne.setTransactionID("APklhYdFZMZ5hDauOrx4")
            walletTransOne.setTransactionDatetime(1664974591)
            walletTransOne.setChargeApplied(0.0)
            walletTransOne.setAmount(1000.00)
            walletTransOne.setAction("BUY")
            walletTransOne.setCardNumber("4763758393205721")
            walletTransOne.setExpiry("12/23")
            walletTransOne.setInitialRate(0.0548)
            walletTransOne.setWalletAddress("hrD3IxwVUWloVP0nrIct")
            walletTransOne.setUnitsSold(0.0)


        cur.close()
        con.commit()
        con.close()

        # Check if the table exists
        #checkTableExistsQuery = "SELECT * FROM information_schema.tables WHERE table_name = 'AvailableCryptocurrency'"
        #cur.execute(checkTableExistsQuery)

    def insertWallet(self, walletObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO Wallet (WalletAddress, CustomerID, InitialBalance, CurrentBalance, " \
                    "CryptocurrencyCode, HoldingPeriod) VALUES(%s, %s, %s, %s,  %s, %s)",
                    (walletObj.getWalletAddress(), walletObj.getCustomerID(), walletObj.getInitialBalance(),
                    walletObj.getCurrentBalance(), walletObj.getCryptocurrencyCode(), walletObj.getHoldingPeriod()))
        cur.close()
        con.commit()
        con.close()

    def insertWalletTransactionHistory(self, walletTransactionObj):
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

    def readAllAvailableCryptocurrency(self):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM AvailableCryptocurrency")
        cryptocurrencies = cur.fetchall()
        cur.close()
        con.commit()
        con.close()
        return cryptocurrencies

    def readWalletFromWalletAddress(self, walletAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Wallet where WalletAddress = %s", walletAddress)
        rowCount = cur.rowcount
        wallet = cur.fetchone()

        cur.close()
        con.commit()
        con.close()

        if rowCount:
            walletOne = Wallet()
            walletOne.setCustomerID(wallet[1])
            walletOne.setWalletAddress(wallet[0])
            walletOne.setInitialBalance(wallet[2])
            walletOne.setCurrentBalance(wallet[3])
            walletOne.setCryptocurrencyCode(wallet[4])
            walletOne.setHoldingPeriod(wallet[5])
            return walletOne
        else:
            raise LookupError("No wallet exists")

    def readWalletsFromCustomerID(self, customerID):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Wallet where customerID = %s", customerID)
        rowCount = cur.rowcount
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
            walletsList = []
            for wallet in result:
                walletOne = Wallet()
                walletOne.setCustomerID(wallet[1])
                walletOne.setWalletAddress(wallet[0])
                walletOne.setInitialBalance(wallet[2])
                walletOne.setCurrentBalance(wallet[3])
                walletOne.setCryptocurrencyCode(wallet[4])
                walletOne.setHoldingPeriod(wallet[5])
                walletsList.append(walletOne)
            return walletsList
        else:
            raise LookupError("No wallet exists")

    def readWalletTransactionsFromWalletAddress(self, walletAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM WalletTransactionHistory where WalletAddress = '"+walletAddress+"'")
        rowCount = cur.rowcount
        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
            walletTransactionsList = []
            for walletTransaction in result:
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
                walletTransactionsList.append(walletTransactionObj)
            return walletTransactionsList
        else:
            raise LookupError("No wallet transaction exists")

    def readPurchaseWalletTransactionFromWalletAddress(self, walletAddress):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM WalletTransactionHistory where Action='BUY' and WalletAddress = '"+walletAddress+"'")
        rowCount = cur.rowcount
        walletTransaction = cur.fetchone()
        cur.close()
        con.commit()
        con.close()

        if rowCount:
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
            return walletTransactionObj
        else:
            raise LookupError("No wallet transaction record exists")

    def updateWalletCurrentBalance(self, walletObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("UPDATE Wallet set CurrentBalance = %s where WalletAddress = %s",
                    (walletObj.getCurrentBalance(), walletObj.getWalletAddress()))
        cur.close()
        con.commit()
        con.close()

    def testDropTables(self):
        # Just for unit testing
        con = self.mysql.connect()
        cur = con.cursor()
        dropQuery = "DROP TABLE Wallet"
        cur.execute(dropQuery)
        dropQuery = "DROP TABLE WalletTransactionHistory"
        cur.execute(dropQuery)
        cur.close()
        con.commit()
        con.close()
