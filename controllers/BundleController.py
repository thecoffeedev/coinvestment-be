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
        dict = {'1': ('Alpha', 'Low risk/Short term'), '2': ('Beta', 'Medium risk/Short term'),
                '3': ('Mu', 'Low risk/Medium term'), '4': ('Omega', 'Medium risk/Medium term'),
                '5': ('Pi', 'Medium risk/Long term'), '6': ('Sigma', 'High risk/Long term')}
        if bundleID in dict.keys():
            return dict[bundleID]
        else:
            raise ValueError("Bundle ID does not exists")

    def getAllAvailableBundles(self):
        try:
            print("getAllAvailableBundles entry")
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
                        "statusMessage": "Bundle sold successfully"
                    },
                    "availableBundles": availableBundles
                }
            print("response :", response)
            return response

        except Exception as e:
            print("getAllAvailableBundles exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("getAllAvailableBundles exception", response)
            return response

    def getAllBundleDetailsFromBundleAddress(self, jsonReqData):
        try:
            print("getAllBundleDetailsFromBundleAddress entry")
            print("jsonReqData : ", jsonReqData)
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            elif not jsonReqData.get("bundleAddress"):
                raise ValueError("Bundle Address not provided in request JSON")
            else:
                bundleFE = Bundle()
                bundleFE.setBundleAddress(jsonReqData.get("bundleAddress"))

                bundleDA = self.BDA.readBundleByBundleAddress(bundleFE.getBundleAddress())
                if jsonReqData.get("customerID") != bundleDA.getCustomerID():
                    raise ValueError("Authorization Error")
                elif "INACTIVE" != bundleDA.getStatus():
                    raise ValueError("Bundle already sold")
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
                            "cardNumber": bundleTransactionObj.getCardNumber(),
                            "expiry": bundleTransactionObj.getExpiry(),
                            "initialRate": bundleTransactionObj.getInitialRate()
                        }
                        bundleTransactionList.append(bundleTransactionDict)

                    print("bundleTransactionList :", bundleTransactionList)

                    response = \
                        {
                            "status": {
                                "statusCode": "SUCCESS",
                                "statusMessage": "Bundle sold successfully"
                            },
                            "bundle": {
                                "bundleAddress": bundleDA.getBundleAddress(),
                                "bundleId": bundleDA.getBundleID(),
                                "customerID": bundleDA.getCustomerID(),
                                "holdingPeriod": bundleDA.getHoldingPeriod(),
                                "purchaseDatetime": Utility.unixTimestampToStrings(bundleDA.getPurchaseDatetime()),
                                "status": bundleDA.getStatus()
                            },
                            "bundleTransaction": bundleTransactionList
                        }
                    print("response :", response)
                    return response

        except Exception as e:
            print("getAllBundleDetailsFromBundleAddress exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("getAllBundleDetailsFromBundleAddress exception", response)
            return response
    
    def getAllBundlesFromCustomerID(self, jsonReqData):
        try:
            print("getAllBundlesFromCustomerID entry")
            print("jsonReqData : ", jsonReqData)
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            else:
                bundleFE = Bundle()
                bundleFE.setCustomerID(jsonReqData.get("customerID"))

                bundleDA = self.BDA.readBundlesByCustomerID(bundleFE.getCustomerID())

                bundleList = []
                for bundleObj in bundleDA:
                    bundleDict = {
                        "bundleAddress": bundleObj.getBundleAddress(),
                        "bundleId": bundleObj.getBundleID(),
                        "customerID": bundleObj.getCustomerID(),
                        "holdingPeriod": bundleObj.getHoldingPeriod(),
                        "purchaseDatetime": Utility.unixTimestampToStrings(bundleObj.getPurchaseDatetime()),
                        "status": bundleObj.getStatus()
                    }
                    bundleList.append(bundleDict)

                print("bundleList :", bundleList)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS",
                            "statusMessage": "Units sold successfully"
                        },
                        "bundle": bundleList
                    }
                print("response :", response)
                return response

        except Exception as e:
            print("getAllBundlesFromCustomerID exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("getAllBundlesFromCustomerID exception", response)
            return response
        print("getAllBundlesFromCustomerID exit")
        
    def purchaseBundle(self, jsonReqData):
        try:
            print("purchaseBundle entry")
            print("jsonReqData : ", jsonReqData)

            bundleFE = Bundle()
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            else:
                bundleFE.setCustomerID(jsonReqData.get("customerID"))

            if not jsonReqData.get("bundleID"):
                raise ValueError("Bundle ID not provided in request JSON")
            else:
                bundleFE.setBundleID(jsonReqData.get("bundleID"))

            if not jsonReqData.get("holdingPeriod"):
                raise ValueError("Holding Period not provided in request JSON")
            else:
                bundleFE.setHoldingPeriod(jsonReqData.get("holdingPeriod"))


            bundleTransactionFE = BundleTransactionHistory()
            if not jsonReqData.get("initialRate"):
                raise ValueError("Initial Rate not provided in request JSON")
            else:
                bundleTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("initialRate")))

            if not jsonReqData.get("amount"):
                raise ValueError("Amount not provided in request JSON")
            else:
                bundleTransactionFE.setAmount(Utility.roundDecimals(jsonReqData.get("amount")))

            if not jsonReqData.get("cardNumber"):
                raise ValueError("Card Number not provided in request JSON")
            else:
                bundleTransactionFE.setCardNumber(jsonReqData.get("cardNumber"))

            if not jsonReqData.get("expiry"):
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

            print("bundleFE : ", bundleFE.__dict__)
            print("bundleTransactionFE : ", bundleTransactionFE.__dict__)
            self.BDA.insertBundle(bundleFE)
            self.BDA.insertBundleTransactionHistory(bundleTransactionFE)

            response = \
                {
                    "status": {
                        "statusCode": "SUCCESS/FAILURE",
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
                        "cardNumber": bundleTransactionFE.getCardNumber(),
                        "expiry": bundleTransactionFE.getExpiry(),
                        "initialRate": bundleTransactionFE.getInitialRate()
                    }
                }
            return response

        except Exception as e:
            print("purchaseBundle exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("purchaseBundle exception", response)
            return response
        print("purchaseBundle exit")

    def sellBundle(self, jsonReqData):
        try:
            print("sellBundle entry")
            print("jsonReqData : ", jsonReqData)

            bundleFE = Bundle()
            bundleTransactionFE = BundleTransactionHistory()
            if not jsonReqData.get("customerID"):
                raise ValueError("Customer ID not provided in request JSON")
            else:
                bundleFE.setCustomerID(jsonReqData.get("customerID"))

            if not jsonReqData.get("bundleAddress"):
                raise ValueError("Bundle Address not provided in request JSON")
            else:
                bundleFE.setBundleAddress(jsonReqData.get("bundleAddress"))

            if not jsonReqData.get("bundleID"):
                raise ValueError("Bundle ID not provided in request JSON")
            else:
                bundleFE.setBundleID(jsonReqData.get("bundleID"))

            bundleFE.setStatus("INACTIVE")
            bundleDA = self.BDA.readBundleByBundleAddress(bundleFE.getBundleAddress())

            if jsonReqData.get("customerID") != bundleDA.getCustomerID():
                raise ValueError("Authorization Error")
            else:
                if not jsonReqData.get("initialRate"):
                    raise ValueError("Initial Rate not provided in request JSON")
                else:
                    bundleTransactionFE.setInitialRate(Utility.roundDecimals(jsonReqData.get("initialRate")))

                if not jsonReqData.get("amount"):
                    raise ValueError("Amount not provided in request JSON")
                else:
                    bundleTransactionFE.setAmount(Utility.roundDecimals(jsonReqData.get("amount")))

                if not jsonReqData.get("cardNumber"):
                    raise ValueError("Card Number not provided in request JSON")
                else:
                    bundleTransactionFE.setCardNumber(jsonReqData.get("cardNumber"))

                if not jsonReqData.get("expiry"):
                    raise ValueError("Expiry not provided in request JSON")
                else:
                    bundleTransactionFE.setExpiry(jsonReqData.get("expiry"))

                bundleTransactionDA = self.BDA.readPurchaseBundleTransactionFromBundleAddress(bundleFE.getBundleAddress())
                bundleTransactionFE.setTransactionID(Utility.generateRandomID())
                bundleTransactionFE.setBundleAddress(bundleFE.getBundleAddress())
                bundleTransactionFE.setTransactionDatetime(int(time.time()))
                if Utility.isWithinHoldingPeriod(bundleTransactionDA.getTransactionDatetime(), bundleDA.getHoldingPeriod()):
                    bundleTransactionFE.setChargeApplied(Utility.calculateChargesApplied(bundleTransactionFE.getAmount()))
                else:
                    bundleTransactionFE.setChargeApplied(Utility.roundDecimals(0.0))
                bundleTransactionFE.setAction("SELL")

                print("bundleFE : ", bundleFE.__dict__)
                print("bundleTransactionFE : ", bundleTransactionFE.__dict__)
                self.BDA.updateBundleStatus(bundleFE)
                self.BDA.insertBundleTransactionHistory(bundleTransactionFE)

                response = \
                    {
                        "status": {
                            "statusCode": "SUCCESS/FAILURE",
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
                            "cardNumber": bundleTransactionFE.getCardNumber(),
                            "expiry": bundleTransactionFE.getExpiry(),
                            "initialRate": bundleTransactionFE.getInitialRate()
                        }
                    }
                return response

        except Exception as e:
            print("sellBundle exception", e)
            response = \
                {
                    "status": {
                        "statusCode": "FAILURE",
                        "statusMessage": e.args[0]
                    }
                }
            print("sellBundle exception", response)
            return response
        print("sellBundle exit")