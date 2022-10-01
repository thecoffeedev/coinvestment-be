from data_access.WalletDataAccess import WalletDataAccess
from models.Wallet import Wallet
from models.Utility import Utility
import requests


class WalletController:

    def __init__(self, app):
        print("__init__ entry")
        self.WDA = WalletDataAccess(app)
        self.generateDayZeroData()
        print("__init__ exit")

    def generateDayZeroData(self):
        print("generateDayZeroData entry")
        self.WDA.generateDayZeroData()
        self.WDA.createWallet()
        self.WDA.insertDayZeroWalletData()
        self.testMethod()
    def testMethod(self):
        try:
            print("createWallet entry")
            self.WDA.insertWallet(None)

        except Exception as e:
            print("createWallet exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("createWallet exception", response)
        print("createWallet exit")

    def purchaseWallet(self, jsonReqData):
        try:
            print("purchaseWallet entry")
            print("jsonReqData : ", jsonReqData)

            walletFE = Wallet()
            if not jsonReqData.get("wallet")["customerID"]:
                raise ValueError("Customer ID not provided in request JSON")
            else:
                walletFE.setCustomerID(jsonReqData.get("customerID"))
            if not jsonReqData.get("initialBalance"):
                raise ValueError("Initial Balance not provided in request JSON")
            else:
                walletFE.setInitialBalance(Utility.roundDecimals(jsonReqData.get("wallet")["initialBalance"]))
            if not jsonReqData.get("cryptocurrencyCode"):
                raise ValueError("Cryptocurrency Code not provided in request JSON")
            else:
                walletFE.setCryptocurrencyCode(jsonReqData.get("wallet")["cryptocurrencyCode"])
            if not jsonReqData.get("holdingPeriod"):
                raise ValueError("Holding Period not provided in request JSON")
            else:
                walletFE.setHoldingPeriod(jsonReqData.get("wallet")["holdingPeriod"])
            walletFE.setWalletAddress(Utility.generateRandomID())
            walletFE.setCurrentBalance(walletFE.getInitialBalance())

            print("walletFE : ", walletFE.__dict__)
            self.WDA.insertWallet()

        except Exception as e:
            print("purchaseWallet exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("purchaseWallet exception", response)
        print("purchaseWallet exit")


