from data_access.BundleDataAccess import BundleDataAccess
import requests


class BundleController:

    def __init__(self, app):
        self.BDA = BundleDataAccess(app)

    def generateDayZeroData(self):

        self.BDA.insertDayZeroData()





    # def createWallet(self):
    #     self.WDA.createWallet()
    #     print("in wallet controller")

