

class Bundle:

    def __init__(self, bundleAddress=None, bundleID=None, customerID = None,
                 amount=None, holdingPeriod=None, purchaseDatetime=None,
                 status=None):
        self.__bundleAddress = bundleAddress
        self.__bundleID = bundleID
        self.__customerID = customerID
        self.__holdingPeriod = holdingPeriod
        self.__purchaseDatetime = purchaseDatetime
        self.__status = status

    def getBundleAddress(self):
        return self.__bundleAddress

    def setBundleAddress(self, bundleAddress):
        if bundleAddress is None:
            raise TypeError("Bundle address must not be none")
        elif type(bundleAddress) != str:
            raise TypeError("Bundle address must be alphanumeric string")
        elif len(str(bundleAddress).strip()) != 20:
            raise ValueError("Bundle address must be exactly 20 characters")
        else:
            self.__bundleAddress = bundleAddress

    def getBundleID(self):
        return self.__bundleID

    def setBundleID(self, bundleID):
        if bundleID is None:
            raise ValueError("Bundle ID must not be none")
        elif type(bundleID) != str:
            raise TypeError("Bundle ID must be a string")
        elif len(str(bundleID).strip()) <= 0:
            raise ValueError("Bundle ID must be atleast 1 character")
        else:
            self.__bundleID = bundleID

    def getCustomerID(self):
        return self.__customerID

    def setCustomerID(self, customerID):
        if customerID is None:
            raise ValueError("Customer ID must not be none")
        elif type(customerID) != str:
            raise TypeError("Customer ID must be alphanumeric string")
        elif len(customerID) != 20:
            raise ValueError("Customer ID must be exactly 20 characters")
        else:
            self.__customerID = customerID

    def getHoldingPeriod(self):
        return self.__holdingPeriod

    def setHoldingPeriod(self, holdingPeriod):
        if holdingPeriod is None:
            raise TypeError("Holding period must not be none")
        elif type(holdingPeriod) != int:
            raise TypeError("Holding period must be an int")
        elif holdingPeriod <= 0:
            raise ValueError("Holding period must not be less than 0")
        else:
            self.__holdingPeriod = holdingPeriod

    def getPurchaseDatetime(self):
        return self.__purchaseDatetime

    def setPurchaseDatetime(self, purchaseDatetime):
        if purchaseDatetime is None:
            raise TypeError("Purchase datetime must not be none")
        elif type(purchaseDatetime) != int:
            raise TypeError("Purchase datetime must be in unix time format, int")
        else:
            self.__purchaseDatetime = purchaseDatetime

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        if status is None:
            raise TypeError("Status must not be none")
        elif type(status) != str:
            raise TypeError("Status must be a string")
        elif str(status).upper() != 'ACTIVE' and str(status).upper() != 'INACTIVE':
            raise ValueError("Status must be 'ACTIVE' or 'INACTIVE'")
        else:
            self.__status = str(status).upper();
