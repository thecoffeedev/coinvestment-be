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

        # self.mysqlDB = MySQL()

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