from models.TransactionHistory import TransactionHistory

class WalletTransactionHistory(TransactionHistory):

    def __init__(self, transactionID=None, transactionDatetime=None, chargeApplied=0.0, amount=0.0,
                 action=None, cardNumber=None, expiry=None, initialRate=None, walletAddress=None, unitsSold=None):
        super().__init__(transactionID, transactionDatetime, chargeApplied, amount,
                         action, cardNumber, expiry, initialRate)

        self.__walletAddress = walletAddress
        self.__unitsSold = unitsSold

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
            
    def getUnitsSold(self):
        return self.__unitsSold

    def setUnitsSold(self, unitsSold):
        if unitsSold is None:
            raise ValueError("Units Sold must not be none")
        if type(unitsSold) != float:
            raise TypeError("Units Sold must be a float")
        elif unitsSold < 0:
            raise ValueError("Units Sold must be greater than or equal zero")
        else:
            self.__unitsSold = unitsSold