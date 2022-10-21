from data_access.BundleDataAccess import BundleDataAccess
from models.Utility import Utility
from models.Bundle import Bundle
from models.BundleTransactionHistory import BundleTransactionHistory
import time
from collections import defaultdict

class BundleController:

    def __init__(self, app):
        self.BDA = BundleDataAccess(app)
        self.BDA.createTables()
        self.BDA.insertDayZeroData()


    def getBundleNameByBundleID(self, bundleID):
        dict = {"1": ["Alpha", "Low risk", "Short term"], "2": ["Beta", "Medium risk", "Short term"],
                "3": ["Mu", "Low risk", "Medium term"], "4": ["Omega", "Medium risk", "Medium term"],
                "5": ["Pi", "Medium risk", "Long term"], "6": ["Sigma", "High risk", "Long term"]}
        if bundleID in dict.keys():
            return dict[bundleID]
        else:
            raise ValueError("Bundle ID does not exists")

    def getAllAvailableBundles(self):
        try:
            availableBundlesDA = self.BDA.readAllAvailableBundles()

            availableBundlesDict = defaultdict(list)

            for availableBundles in availableBundlesDA:
                availableBundlesDict[availableBundles[0]].append(availableBundles)

            availableBundles = []
            for bundleGroup in availableBundlesDict:
                bundleCryptocurrenciesList = []
                for cc in availableBundlesDict[bundleGroup]:
                    bundleCryptocurrencies = {
                        "cryptocurrencyCode": cc[1],
                        "cryptocurrencyName": cc[4],
                        "percentage": cc[2]
                    }
                    bundleCryptocurrenciesList.append(bundleCryptocurrencies)

                bundleNameDict = self.getBundleNameByBundleID(availableBundlesDict[bundleGroup][0][0])
                availableBundle = {
                    "bundleName": bundleNameDict[0],
                    "riskLevel": bundleNameDict[1],
                    "term": bundleNameDict[2],
                    "minimumHoldingPeriod": availableBundlesDict[bundleGroup][0][3],
                    "bundleID": availableBundlesDict[bundleGroup][0][0],
                    "bundleCryptocurrencies": bundleCryptocurrenciesList
                }
                # /coins/{id}/history 180days, 90days, 30days
                availableBundles.append(availableBundle)
            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS",
                        "statusMessage": "All available bundles"
                    },
                    "availableBundles": availableBundles
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

    def getAllBundleDetailsFromBundleAddress(self, jsonReqData):
        try:
            if "customerID" not in jsonReqData.keys():
                raise ValueError("Customer ID not provided in request JSON")
            elif "bundleAddress" not in jsonReqData.keys():
                raise ValueError("Bundle Address not provided in request JSON")
            else:
                bundleFE = Bundle()
                bundleFE.setBundleAddress(jsonReqData.get("bundleAddress"))

                bundleDA = self.BDA.readBundleByBundleAddress(bundleFE.getBundleAddress())
                if jsonReqData.get("customerID") != bundleDA.getCustomerID():
                    raise ValueError("Authorization Error")
                else:
                    bundleTransactionDA = self.BDA.readBundleTransactionsByBundleAddress(bundleFE.getBundleAddress())

                    bundleTransactionList = []
                    for bundleTransactionObj in bundleTransactionDA:
                        bundleTransactionDict = {
                            "transactionID": bundleTransactionObj.getTransactionID(),
                            "transactionDatetime": Utility.unixTimestampToStrings(bundleTransactionObj.getTransactionDatetime()),
                            "chargeApplied": bundleTransactionObj.getChargeApplied(),
                            "amount": bundleTransactionObj.getAmount(),
                            "action": bundleTransactionObj.getAction(),
                            "cardNumber": Utility.maskString(bundleTransactionObj.getCardNumber(), 12),
                            "expiry": Utility.maskString(bundleTransactionObj.getExpiry(), 2),
                            "initialRate": bundleTransactionObj.getInitialRate()
                        }
                        bundleTransactionList.append(bundleTransactionDict)

                    response = \
                        {
                            "status": {
                                "statusCode": "SUCCESS",
                                "statusMessage": "Details for bundle"
                            },
                            "bundle": {
                                "bundleAddress": bundleDA.getBundleAddress(),
                                "bundleID": bundleDA.getBundleID(),
                                "customerID": bundleDA.getCustomerID(),
                                "holdingPeriod": bundleDA.getHoldingPeriod(),
                                "purchaseDatetime": Utility.unixTimestampToStrings(bundleDA.getPurchaseDatetime()),
                                "status": bundleDA.getStatus()
                            },
                            "bundleTransaction": bundleTransactionList
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

    def getAllBundlesFromCustomerID(self, jsonReqData):
        try:
            if "customerID" not in jsonReqData.keys():
                raise ValueError("Customer ID not provided in request JSON")
            else:
                bundleFE = Bundle()
                bundleFE.setCustomerID(jsonReqData.get("customerID"))

                bundleDA = self.BDA.readBundlesByCustomerID(bundleFE.getCustomerID())
                purchaseBundleTransactionDA = self.BDA.readPurchaseBundleTransactionFromBundleAddress(bundleDA[0].getBundleAddress())
                allAvailableBundlesRes = self.getAllAvailableBundles();
                allAvailableBundlesList = allAvailableBundlesRes.get("availableBundles")

                bundleList = []
                for bundleObj in bundleDA:
                    availableBundleObj = {}
                    for availableBundle in allAvailableBundlesList:
                        if bundleObj.getBundleID() == availableBundle.get("bundleID"):
                            availableBundleObj = availableBundle
                            break

                    bundleDict = {
                        "bundleAddress": bundleObj.getBundleAddress(),
                        "bundleID": bundleObj.getBundleID(),
                        "customerID": bundleObj.getCustomerID(),
                        "holdingPeriod": bundleObj.getHoldingPeriod(),
                        "purchaseDatetime": Utility.unixTimestampToStrings(bundleObj.getPurchaseDatetime()),
                        "status": bundleObj.getStatus(),
                        "amount": Utility.roundDecimals(purchaseBundleTransactionDA.getAmount()),
                        "bundleName": availableBundleObj.get("bundleName"),
                        "riskLevel": availableBundleObj.get("riskLevel"),
                        "term": availableBundleObj.get("term"),
                        "minimumHoldingPeriod": availableBundleObj.get("minimumHoldingPeriod"),
                        "bundleCryptocurrencies": availableBundleObj.get("bundleCryptocurrencies")
                    }
                    bundleList.append(bundleDict)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "All bundles for customer"
                        },
                        "bundles": bundleList
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
        
    def purchaseBundle(self, jsonReqData):
        try:
            bundleFE = Bundle()
            if "customerID" not in jsonReqData.keys():
                raise ValueError("Customer ID not provided in request JSON")
            else:
                bundleFE.setCustomerID(jsonReqData.get("customerID"))

            if "bundleID" not in jsonReqData.keys():
                raise ValueError("Bundle ID not provided in request JSON")
            else:
                bundleFE.setBundleID(jsonReqData.get("bundleID"))

            if not jsonReqData.get("holdingPeriod"):
                raise ValueError("Holding Period not provided in request JSON")
            else:
                bundleFE.setHoldingPeriod(jsonReqData.get("holdingPeriod"))


            bundleTransactionFE = BundleTransactionHistory()
            if "initialRate" not in jsonReqData.keys():
                raise ValueError("Initial Rate not provided in request JSON")
            else:
                bundleTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("initialRate")))

            if "amount" not in jsonReqData.keys():
                raise ValueError("Amount not provided in request JSON")
            else:
                bundleTransactionFE.setAmount(Utility.roundDecimals(jsonReqData.get("amount")))

            if "cardNumber" not in jsonReqData.keys():
                raise ValueError("Card Number not provided in request JSON")
            else:
                bundleTransactionFE.setCardNumber(jsonReqData.get("cardNumber"))

            if "expiry" not in jsonReqData.keys():
                raise ValueError("Expiry not provided in request JSON")
            else:
                bundleTransactionFE.setExpiry(jsonReqData.get("expiry"))

            timeNow = int(time.time())
            transactionID = Utility.generateRandomID()
            bundleAddress = Utility.generateRandomID()

            bundleFE.setBundleAddress(bundleAddress)
            bundleFE.setPurchaseDatetime(timeNow)
            bundleFE.setStatus("ACTIVE")

            bundleTransactionFE.setTransactionID(transactionID)
            bundleTransactionFE.setBundleAddress(bundleAddress)
            bundleTransactionFE.setTransactionDatetime(timeNow)
            bundleTransactionFE.setChargeApplied(Utility.roundDecimals(0.0))
            bundleTransactionFE.setAction("BUY")

            self.BDA.insertBundle(bundleFE)
            self.BDA.insertBundleTransactionHistory(bundleTransactionFE)

            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS",
                        "statusMessage": "Bundle purchased successfully"
                    },
                    "bundle": {
                        "bundleAddress": bundleFE.getBundleAddress(),
                        "customerID": bundleFE.getCustomerID(),
                        "bundleID": bundleFE.getBundleID(),
                        "purchaseDatetime": Utility.unixTimestampToStrings(bundleFE.getPurchaseDatetime()),
                        "status": bundleFE.getStatus(),
                        "holdingPeriod": bundleFE.getHoldingPeriod()
                    },
                    "bundleTransaction": {
                        "transactionID": bundleTransactionFE.getTransactionID(),
                        "transactionDatetime": Utility.unixTimestampToStrings(bundleTransactionFE.getTransactionDatetime()),
                        "chargeApplied": bundleTransactionFE.getChargeApplied(),
                        "amount": bundleTransactionFE.getAmount(),
                        "action": bundleTransactionFE.getAction(),
                        "cardNumber": Utility.maskString(bundleTransactionFE.getCardNumber(), 12),
                        "expiry": Utility.maskString(bundleTransactionFE.getExpiry(), 2),
                        "initialRate": bundleTransactionFE.getInitialRate()
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

    def sellBundle(self, jsonReqData):
        try:
            bundleFE = Bundle()
            bundleTransactionFE = BundleTransactionHistory()
            if "customerID" not in jsonReqData.keys():
                raise ValueError("Customer ID not provided in request JSON")
            else:
                bundleFE.setCustomerID(jsonReqData.get("customerID"))

            if "bundleAddress" not in jsonReqData.keys():
                raise ValueError("Bundle Address not provided in request JSON")
            else:
                bundleFE.setBundleAddress(jsonReqData.get("bundleAddress"))

            if "bundleID" not in jsonReqData.keys():
                raise ValueError("Bundle ID not provided in request JSON")
            else:
                bundleFE.setBundleID(jsonReqData.get("bundleID"))

            bundleFE.setStatus("INACTIVE")
            bundleDA = self.BDA.readBundleByBundleAddress(bundleFE.getBundleAddress())

            if jsonReqData.get("customerID") != bundleDA.getCustomerID():
                raise ValueError("Authorization Error")
            else:
                if "initialRate" not in jsonReqData.keys():
                    raise ValueError("Initial Rate not provided in request JSON")
                else:
                    bundleTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("initialRate")))

                if "amount" not in jsonReqData.keys():
                    raise ValueError("Amount not provided in request JSON")
                else:
                    bundleTransactionFE.setAmount(Utility.roundDecimals(jsonReqData.get("amount")))

                if "cardNumber" not in jsonReqData.keys():
                    raise ValueError("Card Number not provided in request JSON")
                else:
                    bundleTransactionFE.setCardNumber(jsonReqData.get("cardNumber"))

                if "expiry" not in jsonReqData.keys():
                    raise ValueError("Expiry not provided in request JSON")
                else:
                    bundleTransactionFE.setExpiry(jsonReqData.get("expiry"))

                bundleTransactionDA = self.BDA.readPurchaseBundleTransactionFromBundleAddress(bundleFE.getBundleAddress())
                bundleTransactionFE.setTransactionID(Utility.generateRandomID())
                bundleTransactionFE.setBundleAddress(bundleFE.getBundleAddress())
                bundleTransactionFE.setTransactionDatetime(int(time.time()))
                if Utility.isWithinHoldingPeriod(bundleTransactionDA.getTransactionDatetime(), bundleDA.getHoldingPeriod()):
                    bundleTransactionFE.setChargeApplied(Utility.calculateDeduction(bundleTransactionFE.getAmount(), float(0.10)))
                else:
                    bundleTransactionFE.setChargeApplied(Utility.calculateDeduction(bundleTransactionFE.getAmount(), float(0.01)))
                bundleTransactionFE.setAction("SELL")

                self.BDA.updateBundleStatus(bundleFE)
                self.BDA.insertBundleTransactionHistory(bundleTransactionFE)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "Bundle sold successfully"
                        },
                        "bundle": {
                            "bundleAddress": bundleFE.getBundleAddress(),
                            "customerID": bundleFE.getCustomerID(),
                            "bundleID": bundleFE.getBundleID(),
                            "purchaseDatetime": Utility.unixTimestampToStrings(bundleDA.getPurchaseDatetime()),
                            "status": bundleFE.getStatus(),
                            "holdingPeriod": bundleDA.getHoldingPeriod()
                        },
                        "bundleTransaction": {
                            "transactionID": bundleTransactionFE.getTransactionID(),
                            "transactionDatetime": Utility.unixTimestampToStrings(bundleTransactionFE.getTransactionDatetime()),
                            "chargeApplied": bundleTransactionFE.getChargeApplied(),
                            "amount": bundleTransactionFE.getAmount(),
                            "action": bundleTransactionFE.getAction(),
                            "cardNumber": Utility.maskString(bundleTransactionFE.getCardNumber(), 12),
                            "expiry": Utility.maskString(bundleTransactionFE.getExpiry(), 2),
                            "initialRate": bundleTransactionFE.getInitialRate()
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
