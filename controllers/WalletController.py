from data_access.WalletDataAccess import WalletDataAccess
import requests


class WalletController:

    def __init__(self, app):
        self.WDA = WalletDataAccess(app)
        # self.WDA.generateDayZeroData()

    def createWallet(self):
        self.WDA.createWallet()
        print("in wallet controller")

