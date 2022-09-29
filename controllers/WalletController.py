from data_access.WalletDataAccess import WalletDataAccess
import requests


class WalletController:

    def __init__(self, app):
        self.WDA = WalletDataAccess(app)

    def dayZeroData(self):
        # url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&order=market_cap_desc&per_page=50&page=1&sparkline=false"
        # res = requests.get(url).json()
        #
        # for item in currencyList:
        #     currencyList.append([item["symbol"], item["name"]])
        #
        # print(currencyList)

        self.WDA.generateDayZeroData()





    # def createWallet(self):
    #     self.WDA.createWallet()
    #     print("in wallet controller")

