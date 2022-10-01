import string


class Wallet:

    def __init__(self, walletAddress=None, customerID=None, initialBalance=0.0,
                 currentBalance=0.0, cryptocurrencyCode=None, holdingPeriod=0):
        self.__walletAddress = walletAddress
        self.__customerID = customerID
        self.__initialBalance = initialBalance
        self.__currentBalance = currentBalance
        self.__cryptocurrencyCode = cryptocurrencyCode
        self.__holdingPeriod = holdingPeriod

    # getter method
    def getWalletAddress(self):
        return self.__walletAddress

    # setter method
    def setWalletAddress(self, walletAddress):
        if walletAddress is None:
            raise ValueError("Wallet Address must not be none")
        elif type(walletAddress) != str:
            raise TypeError("Wallet Address must be alphanumeric string")
        elif len(walletAddress) != 20:
            raise ValueError("Wallet Address must be exactly 20 characters")
        else:
            self.__walletAddress = walletAddress

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

    def getInitialBalance(self):
        return self.__initialBalance

    def setInitialBalance(self, initialBalance):
        if initialBalance is None:
            raise ValueError("Initial Balance must not be none")
        if type(initialBalance) != float:
            raise TypeError("Initial Balance must be a float")
        elif initialBalance <= 0:
            raise ValueError("Initial Balance must be greater than zero")
        else:
            self.__initialBalance = initialBalance

    def getCurrentBalance(self):
        return self.__currentBalance

    def setCurrentBalance(self, currentBalance):
        if currentBalance is None:
            raise ValueError("Current Balance must not be none")
        elif type(currentBalance) != float:
            raise TypeError("Current Balance must be an float")
        elif currentBalance < 0:
            raise ValueError("Current Balance must be greater than or equal to zero")
        else:
            self.__currentBalance = currentBalance

    def getCryptocurrencyCode(self):
        return self.__cryptocurrencyCode

    def setCryptocurrencyCode(self, cryptocurrencyCode):
        if cryptocurrencyCode is None or len(str(cryptocurrencyCode).strip()) <= 0:
            raise ValueError("Cryptocurrency Code must not be none or empty")
        elif type(cryptocurrencyCode) != str:
            raise TypeError("Cryptocurrency Code must be alphanumeric string")
        elif len(cryptocurrencyCode) > 10:
            raise ValueError("Cryptocurrency Code must be less than or equal to 10 characters")
        elif len(cryptocurrencyCode) <= 2:
            raise ValueError("Cryptocurrency Code must be more than 2 characters")
        else:
            self.__cryptocurrencyCode = cryptocurrencyCode

    def getHoldingPeriod(self):
        return self.__holdingPeriod

    def setHoldingPeriod(self, holdingPeriod):
        if holdingPeriod is None:
            raise ValueError("Holding Period must not be none")
        elif type(holdingPeriod) != int:
            raise TypeError("Holding Period must be an integer")
        elif holdingPeriod <= 0:
            raise ValueError("Holding Period must be greater than zero")
        else:
            self.__holdingPeriod = holdingPeriod
