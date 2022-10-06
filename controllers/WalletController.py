from flask import json

from data_access.WalletDataAccess import WalletDataAccess
from models.Wallet import Wallet
from models.Utility import Utility
from models.WalletTransactionHistory import WalletTransactionHistory
import time


class WalletController:

    def __init__(self, app):
        self.WDA = WalletDataAccess(app)
        self.WDA.createTables()
        self.WDA.insertDayZeroData()

    def getAllAvailableCryptocurrencies(self):
        try:
            available = self.WDA.readAllAvailableCryptocurrency()
            availableCryptocurrencies = []

            for cc in available:
                cryptoDict = {
                    "cryptocurrencyCode": cc[0],
                    "cryptocurrencyName": cc[1],
                    "sybbol": cc[2]
                }
                availableCryptocurrencies.append(cryptoDict)

            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS",
                        "statusMessage": "List of all available cryptocurrencies"
                    },
                    "availableCryptocurrencies": availableCryptocurrencies
                }
            return response

        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def getAllWalletDetailsFromWalletAddress(self, jsonReqData):
        try:
            if not jsonReqData.get("walletAddress"):
                raise ValueError("Wallet address not provided in request JSON")
            else:
                walletFE = Wallet()
                walletFE.setWalletAddress(jsonReqData.get("walletAddress"))

                walletDA = self.WDA.readWalletFromWalletAddress(walletFE.getWalletAddress())
                walletTransactionDA = self.WDA.readWalletTransactionsFromWalletAddress(walletFE.getWalletAddress())

                walletTransactionList = []
                for walletTransactionObj in walletTransactionDA:
                    walletTransactionDict = {
                        "transactionID": walletTransactionObj.getTransactionID(),
                        "transactionDatetime": Utility.unixTimestampToStrings(walletTransactionObj.getTransactionDatetime()),
                        "chargeApplied": walletTransactionObj.getChargeApplied(),
                        "amount": walletTransactionObj.getAmount(),
                        "action": walletTransactionObj.getAction(),
                        "cardNumber": walletTransactionObj.getCardNumber(),
                        "expiry": walletTransactionObj.getExpiry(),
                        "unitsSold": walletTransactionObj.getUnitsSold(),
                        "initialRate": walletTransactionObj.getInitialRate()
                    }
                    walletTransactionList.append(walletTransactionDict)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "All wallet details"
                        },
                        "wallet": {
                            "walletAddress": walletDA.getWalletAddress(),
                            "customerID": walletDA.getCustomerID(),
                            "initialBalance": walletDA.getInitialBalance(),
                            "currentBalance": walletDA.getCurrentBalance(),
                            "cryptocurrencyCode": walletDA.getCryptocurrencyCode(),
                            "holdingPeriod": walletDA.getHoldingPeriod()
                        },
                        "walletTransactions": walletTransactionList
                    }
                return response

        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def getAllWalletsFromCustomerID(self, jsonReqData):
        try:
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            else:
                walletFE = Wallet()
                walletFE.setCustomerID(jsonReqData.get("customerID"))

                walletDA = self.WDA.readWalletsFromCustomerID(walletFE.getCustomerID())

                walletList = []
                for walletObj in walletDA:
                    walletDict = {
                        "walletAddress": walletObj.getWalletAddress(),
                        "customerID": walletObj.getCustomerID(),
                        "initialBalance": walletObj.getInitialBalance(),
                        "currentBalance": walletObj.getCurrentBalance(),
                        "cryptocurrencyCode": walletObj.getCryptocurrencyCode(),
                        "holdingPeriod": walletObj.getHoldingPeriod()
                    }
                    walletList.append(walletDict)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "All wallets for customer"
                        },
                        "wallet": walletList
                    }
                return response

        except Exception as e:
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def purchaseWallet(self, jsonReqData):
        try:
            walletFE = Wallet()
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            else:
                walletFE.setCustomerID(jsonReqData.get("customerID"))

            if not jsonReqData.get("initialBalance"):
                raise ValueError("Initial Balance not provided in request JSON")
            else:
                walletFE.setInitialBalance(Utility.roundDecimals(jsonReqData.get("initialBalance")))

            if not jsonReqData.get("cryptocurrencyCode"):
                raise ValueError("Cryptocurrency Code not provided in request JSON")
            else:
                walletFE.setCryptocurrencyCode(jsonReqData.get("cryptocurrencyCode"))

            if not jsonReqData.get("holdingPeriod"):
                raise ValueError("Holding Period not provided in request JSON")
            else:
                walletFE.setHoldingPeriod(jsonReqData.get("holdingPeriod"))


            walletTransactionFE = WalletTransactionHistory()
            if not jsonReqData.get("initialRate"):
                raise ValueError("Initial Rate not provided in request JSON")
            else:
                walletTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("initialRate")))

            if not jsonReqData.get("amount"):
                raise ValueError("Amount not provided in request JSON")
            else:
                walletTransactionFE.setAmount(Utility.roundDecimals(jsonReqData.get("amount")))

            if not jsonReqData.get("cardNumber"):
                raise ValueError("Card Number not provided in request JSON")
            else:
                walletTransactionFE.setCardNumber(jsonReqData.get("cardNumber"))

            if not jsonReqData.get("expiry"):
                raise ValueError("Expiry not provided in request JSON")
            else:
                walletTransactionFE.setExpiry(jsonReqData.get("expiry"))

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

            self.WDA.insertWallet(walletFE)
            self.WDA.insertWalletTransactionHistory(walletTransactionFE)

            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS/FAILURE",
                        "statusMessage": "Cryptocurrency purchased"
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
                        "transactionDatetime": Utility.unixTimestampToStrings(walletTransactionFE.getTransactionDatetime()),
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
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response

    def sellWallet(self, jsonReqData):
        try:
            walletFE = Wallet()
            walletTransactionFE = WalletTransactionHistory()
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            else:
                walletFE.setCustomerID(jsonReqData.get("customerID"))

            if not jsonReqData.get("walletAddress"):
                raise ValueError("Wallet Address not provided in request JSON")
            else:
                walletFE.setWalletAddress(jsonReqData.get("walletAddress"))

            walletDA = self.WDA.readWalletFromWalletAddress(walletFE.getWalletAddress())

            if not jsonReqData.get("unitsSold"):
                raise ValueError("Units Sold not provided in request JSON")
            else:
                walletTransactionFE.setUnitsSold(Utility.roundDecimals(jsonReqData.get("unitsSold")))

            if walletTransactionFE.getUnitsSold() == 0:
                raise ValueError("Units Sold must be greater than zero")
            elif walletDA.getCurrentBalance() == 0:
                raise ValueError("Action cannot be carried out on Inactive wallets")
            elif walletTransactionFE.getUnitsSold() > walletDA.getCurrentBalance():
                raise ValueError("Units to sell must not be greater than the Current Balance")
            else:
                walletFE.setCurrentBalance(Utility.roundDecimals(float(walletDA.getCurrentBalance()) - float(walletTransactionFE.getUnitsSold())))


            if not jsonReqData.get("initialRate"):
                raise ValueError("Initial Rate not provided in request JSON")
            else:
                walletTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("initialRate")))

            if not jsonReqData.get("amount"):
                raise ValueError("Amount not provided in request JSON")
            else:
                walletTransactionFE.setAmount(
                    Utility.roundDecimals(float(walletTransactionFE.getUnitsSold()) * float(walletTransactionFE.getInitialRate())))

            if not jsonReqData.get("cardNumber"):
                raise ValueError("Card Number not provided in request JSON")
            else:
                walletTransactionFE.setCardNumber(jsonReqData.get("cardNumber"))

            if not jsonReqData.get("expiry"):
                raise ValueError("Expiry not provided in request JSON")
            else:
                walletTransactionFE.setExpiry(jsonReqData.get("expiry"))

            walletTransactionDA = self.WDA.readPurchaseWalletTransactionFromWalletAddress(walletFE.getWalletAddress())
            walletTransactionFE.setTransactionID(Utility.generateRandomID())
            walletTransactionFE.setWalletAddress(walletFE.getWalletAddress())
            walletTransactionFE.setTransactionDatetime(int(time.time()))
            if Utility.isWithinHoldingPeriod(walletTransactionDA.getTransactionDatetime(), walletDA.getHoldingPeriod()):
                walletTransactionFE.setChargeApplied(Utility.calculateChargesApplied(walletTransactionFE.getAmount()))
            else:
                walletTransactionFE.setChargeApplied(Utility.roundDecimals(0.0))
            walletTransactionFE.setAction("SELL")

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
                        "transactionDatetime": Utility.unixTimestampToStrings(walletTransactionFE.getTransactionDatetime()),
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
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            return response


