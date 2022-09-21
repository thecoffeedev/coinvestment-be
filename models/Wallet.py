
class Wallet:

    def __init__(self):
        self.walletAddress = None
        self.userId = None
        self.initialBalance = 0.0
        self.currentBalance = 0.0
        self.cryptocurrencyCode = None
        self.holdingPeriod = 0

    #parameterized constructor
    # def __init__(self, walletAddress, userId, initialBalance, currentBalance, cryptocurrencyCode, holdingPeriod):
    #     self.walletAddress = walletAddress
    #     self.userId = userId
    #     self.initialBalance = initialBalance
    #     self.currentBalance = currentBalance
    #     self.cryptocurrencyCode = cryptocurrencyCode
    #     self.holdingPeriod = holdingPeriod

    # @property
    # def walletAddress(self):
    #     return self.walletAddress
    #
    # @walletAddress.setter
    # def walletAddress(self, walletAddress):
    #     self.walletAddress = walletAddress

    # getter method
    def get_walletAddress(self):
        return self.__walletAddress

    # setter method
    def set_walletAddress(self, walletAddress):
        self.__walletAddress = walletAddress