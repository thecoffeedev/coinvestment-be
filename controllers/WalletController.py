from data_access.WalletDataAccess import WalletDataAccess
from models.Wallet import Wallet
from models.Utility import Utility
from models.WalletTransactionHistory import WalletTransactionHistory
import time


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
        self.WDA.createWalletTransactionHistory()
        # self.WDA.insertDayZeroWalletData()
        # self.testMethod()

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
                walletFE.setCustomerID(jsonReqData.get("wallet")["customerID"])

            if not jsonReqData.get("wallet")["initialBalance"]:
                raise ValueError("Initial Balance not provided in request JSON")
            else:
                walletFE.setInitialBalance(Utility.roundDecimals(jsonReqData.get("wallet")["initialBalance"]))

            if not jsonReqData.get("wallet")["cryptocurrencyCode"]:
                raise ValueError("Cryptocurrency Code not provided in request JSON")
            else:
                walletFE.setCryptocurrencyCode(jsonReqData.get("wallet")["cryptocurrencyCode"])

            if not jsonReqData.get("wallet")["holdingPeriod"]:
                raise ValueError("Holding Period not provided in request JSON")
            else:
                walletFE.setHoldingPeriod(jsonReqData.get("wallet")["holdingPeriod"])


            walletTransactionFE = WalletTransactionHistory()
            if not jsonReqData.get("walletTransaction")["initialRate"]:
                raise ValueError("Initial Rate not provided in request JSON")
            else:
                walletTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("walletTransaction")["initialRate"]))

            if not jsonReqData.get("walletTransaction")["amount"]:
                raise ValueError("Amount not provided in request JSON")
            else:
                walletTransactionFE.setAmount(Utility.roundDecimals(jsonReqData.get("walletTransaction")["amount"]))

            if not jsonReqData.get("walletTransaction")["cardNumber"]:
                raise ValueError("Card Number not provided in request JSON")
            else:
                walletTransactionFE.setCardNumber(jsonReqData.get("walletTransaction")["cardNumber"])

            if not jsonReqData.get("walletTransaction")["expiry"]:
                raise ValueError("Expiry not provided in request JSON")
            else:
                walletTransactionFE.setExpiry(jsonReqData.get("walletTransaction")["expiry"])

            timeNow = int(time.time())
            transactionID = Utility.generateRandomID()
            walletAddress = Utility.generateRandomID()

            walletFE.setWalletAddress(walletAddress)
            walletFE.setCurrentBalance(walletFE.getInitialBalance())
            walletFE.setInitialBalance(Utility.roundDecimals(float(walletTransactionFE.getAmount()) / float(walletTransactionFE.getInitialRate())))
            walletFE.setCurrentBalance(walletFE.getInitialBalance())

            walletTransactionFE.setTransactionID(transactionID)
            walletTransactionFE.setWalletAddress(walletAddress)
            walletTransactionFE.setTransactionDatetime(timeNow)
            walletTransactionFE.setChargeApplied(Utility.roundDecimals(0.0))
            walletTransactionFE.setAction("BUY")
            walletTransactionFE.setUnitsSold(Utility.roundDecimals(0.0))

            print("walletFE : ", walletFE.__dict__)
            print("walletTransactionFE : ", walletTransactionFE.__dict__)
            self.WDA.insertWallet(walletFE)
            self.WDA.insertWalletTransactionHistory(walletTransactionFE)

            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS/FAILURE",
                        "statusMessage": "Units sold successfully"
                    },
                    "wallet": {
                        "walletAddress": walletFE.getWalletAddress(),
                        "customerID": walletFE.getCustomerID(),
                        "initialBalance": walletFE.getInitialBalance(),
                        "currentBalance": walletFE.getCurrentBalance(),
                        "cryptocurrencyCode": walletFE.getCryptocurrencyCode(),
                        "holdingPeriod": walletFE.getHoldingPeriod()
                    },
                    "walletTransaction": {
                        "transactionID": walletTransactionFE.getTransactionID(),
                        "transactionDateTime": Utility.unixTimestampToStrings(walletTransactionFE.getTransactionDatetime()),
                        "chargeApplied": walletTransactionFE.getChargeApplied(),
                        "amount": walletTransactionFE.getAmount(),
                        "action": walletTransactionFE.getAmount(),
                        "cardNumber": walletTransactionFE.getCardNumber(),
                        "expiry": walletTransactionFE.getExpiry(),
                        "unitsSold": walletTransactionFE.getUnitsSold(),
                        "initialRate": walletTransactionFE.getInitialRate()
                    }
                }
            return response

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

    def sellWallet(self, jsonReqData):
        try:
            print("sellWallet entry")
            print("jsonReqData : ", jsonReqData)

            walletFE = Wallet()
            walletTransactionFE = WalletTransactionHistory()
            if not jsonReqData.get("wallet")["customerID"]:
                raise ValueError("Customer ID not provided in request JSON")
            else:
                walletFE.setCustomerID(jsonReqData.get("wallet")["customerID"])

            if not jsonReqData.get("wallet")["walletAddress"]:
                raise ValueError("Wallet Address not provided in request JSON")
            else:
                walletFE.setWalletAddress(jsonReqData.get("wallet")["walletAddress"])

            walletDA = self.WDA.readWalletFromWalletAddress(walletFE.getWalletAddress())

            if not jsonReqData.get("walletTransaction")["unitsSold"]:
                raise ValueError("Units Sold not provided in request JSON")
            else:
                walletTransactionFE.setUnitsSold(Utility.roundDecimals(jsonReqData.get("walletTransaction")["unitsSold"]))

            if walletTransactionFE.getUnitsSold() == 0:
                raise ValueError("Units Sold must be greater than zero")
            elif walletDA.getCurrentBalance() == 0:
                raise ValueError("Action cannot be carried out on Inactive wallets")
            elif walletTransactionFE.getUnitsSold() > walletDA.getCurrentBalance():
                raise ValueError("Units to sell must not be greater than the Current Balance")
            else:
                walletFE.setCurrentBalance(Utility.roundDecimals(float(walletDA.getCurrentBalance()) - float(walletTransactionFE.getUnitsSold())))


            if not jsonReqData.get("walletTransaction")["initialRate"]:
                raise ValueError("Initial Rate not provided in request JSON")
            else:
                walletTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("walletTransaction")["initialRate"]))

            if not jsonReqData.get("walletTransaction")["amount"]:
                raise ValueError("Amount not provided in request JSON")
            else:
                walletTransactionFE.setAmount(
                    Utility.roundDecimals(float(walletTransactionFE.getUnitsSold()) * float(walletTransactionFE.getInitialRate())))

            if not jsonReqData.get("walletTransaction")["cardNumber"]:
                raise ValueError("Card Number not provided in request JSON")
            else:
                walletTransactionFE.setCardNumber(jsonReqData.get("walletTransaction")["cardNumber"])

            if not jsonReqData.get("walletTransaction")["expiry"]:
                raise ValueError("Expiry not provided in request JSON")
            else:
                walletTransactionFE.setExpiry(jsonReqData.get("walletTransaction")["expiry"])

            walletTransactionDA = self.WDA.readPurchaseWalletTransactionFromWalletAddress(walletFE.getWalletAddress())
            walletTransactionFE.setTransactionID(Utility.generateRandomID())
            walletTransactionFE.setWalletAddress(walletFE.getWalletAddress())
            walletTransactionFE.setTransactionDatetime(int(time.time()))
            if Utility.isWithinHoldingPeriod(walletTransactionDA.getTransactionDatetime(), walletDA.getHoldingPeriod()):
                walletTransactionFE.setChargeApplied(Utility.calculateChargesApplied(walletTransactionFE.getAmount()))
            else:
                walletTransactionFE.setChargeApplied(Utility.roundDecimals(0.0))
            walletTransactionFE.setAction("SELL")

            print("walletFE : ", walletFE.__dict__)
            print("walletTransactionFE : ", walletTransactionFE.__dict__)
            self.WDA.updateWalletCurrentBalance(walletFE)
            self.WDA.insertWalletTransactionHistory(walletTransactionFE)

            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS/FAILURE",
                        "statusMessage": "Units sold successfully"
                    },
                    "wallet": {
                        "walletAddress": walletFE.getWalletAddress(),
                        "customerID": walletFE.getCustomerID(),
                        "initialBalance": walletDA.getInitialBalance(),
                        "currentBalance": walletFE.getCurrentBalance(),
                        "cryptocurrencyCode": walletDA.getCryptocurrencyCode(),
                        "holdingPeriod": walletDA.getHoldingPeriod()
                    },
                    "walletTransaction": {
                        "transactionID": walletTransactionFE.getTransactionID(),
                        "transactionDateTime": Utility.unixTimestampToStrings(walletTransactionFE.getTransactionDatetime()),
                        "chargeApplied": walletTransactionFE.getChargeApplied(),
                        "amount": walletTransactionFE.getAmount(),
                        "action": walletTransactionFE.getAmount(),
                        "cardNumber": walletTransactionFE.getCardNumber(),
                        "expiry": walletTransactionFE.getExpiry(),
                        "unitsSold": walletTransactionFE.getUnitsSold(),
                        "initialRate": walletTransactionFE.getInitialRate()
                    }
                }
            return response

        except Exception as e:
            print("sellWallet exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("sellWallet exception", response)
        print("sellWallet exit")


