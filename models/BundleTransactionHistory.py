from models.TransactionHistory import TransactionHistory


class BundleTransactionHistory(TransactionHistory):

    def __init__(self, transactionID=None, transactionDateTime=None, chargeApplied=0.0,
                 amount=0.0, action=None, cardNumber=None, expiry=None, bundleAddress=None):
        super().__init__(transactionID, transactionDateTime, chargeApplied,
                         amount, action, cardNumber, expiry)

        self.__bundleAddress = bundleAddress

    def getBundleAddress(self):
        return self.__bundleAddress

    # setter method
    def setBundleAddress(self, bundleAddress):
        if bundleAddress is None:
            raise ValueError("Bundle Address must not be none")
        elif type(bundleAddress) != str:
            raise TypeError("Bundle Address must be alphanumeric string")
        elif len(bundleAddress) != 20:
            raise ValueError("Bundle Address must be exactly 20 characters")
        else:
            self.__bundleAddress = bundleAddress
