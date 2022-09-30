from flaskext.mysql import MySQL
from models.Wallet import Wallet
from models.Utility import Utility
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

        self.generateDayZeroData()
        self.createWallet()
        self.insertDayZeroWalletData()
        self.readWalletFromWalletAddress("UazgXbwu2tloBcajCPb8")
        self.readWalletFromCustomerID("Debo32tKqJBeZwHHgkvx")

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

    def testMethod(self):
        createQuery = "SELECT * from testInsert1"
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute(createQuery)
        myresult = cur.fetchall()

        for x in myresult:
            print(x)
            print(x[0])

    def createWallet(self):
        print("createWallet entry")
        createTableQuery = "CREATE TABLE IF NOT EXISTS Wallet (" \
                           "WalletAddress VARCHAR(20), " \
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
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO Wallet (WalletAddress, CustomerID, InitialBalance, CurrentBalance, " \
                    "CryptocurrencyCode, HoldingPeriod) VALUES(%s, %s, %s, %s,  %s, %s)",
                    (walletObj.getWalletAddress(), walletObj.getCustomerID(), walletObj.getInitialBalance(),
                    walletObj.getCurrentBalance(), walletObj.getCryptocurrencyCode(), walletObj.getHoldingPeriod()))
        cur.close()
        con.commit()
        con.close()

    def readWalletFromWalletAddress(self, walletObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Wallet where WalletAddress = '"+walletObj.getWalletAddress()+"'")

        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

        for wallet in result:
            print(wallet)
            walletOne = Wallet()
            walletOne.setCustomerID(wallet[1])
            walletOne.setWalletAddress(wallet[0])
            print("wallet address ", wallet[0])
            walletOne.setInitialBalance(wallet[2])
            walletOne.setCurrentBalance(wallet[3])
            walletOne.setCryptocurrencyCode(wallet[4])
            walletOne.setHoldingPeriod(wallet[5])
            print(walletOne)

    def readWalletFromCustomerID(self, walletObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM Wallet where customerID = '"+walletObj.getCurrentBalance()+"'")

        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()

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

    def updateWalletCurrentBalance(self, walletObj):
        con = self.mysql.connect()
        cur = con.cursor()
        cur.execute("UPDATE Wallet set CurrentBalance = '"+walletObj.getCurrentBalance()+
                    "' where WalletAddress = '"+walletObj.getWalletAddress()+"'")

        result = cur.fetchall()
        cur.close()
        con.commit()
        con.close()
