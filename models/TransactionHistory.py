import re

class TransactionHistory:

    def __init__(self, transactionID=None, transactionDatetime=None, chargeApplied=0.0, amount=0.0,
                 action=None, cardNumber=None, expiry=None, initialRate=None):
        self._transactionID = transactionID
        self._transactionDatetime = transactionDatetime
        self._chargeApplied = chargeApplied
        self._amount = amount
        self._action = action
        self._cardNumber = cardNumber
        self._expiry = expiry
        self._initialRate = initialRate

    def getTransactionID(self):
        return self._transactionID

    def setTransactionID(self, transactionID):
        if transactionID is None:
            raise ValueError("Transaction ID must not be none")
        elif type(transactionID) != str:
            raise TypeError("Transaction ID must be alphanumeric string")
        elif len(transactionID) != 20:
            raise ValueError("Transaction ID must be exactly 20 characters")
        else:
            self._transactionID = transactionID

    def getTransactionDatetime(self):
        return self._transactionDatetime

    def setTransactionDatetime(self, transactionDatetime):
        if transactionDatetime is None:
            raise TypeError("Transaction datetime must not be none")
        elif type(transactionDatetime) != int:
            raise TypeError("Transaction datetime must be in unix time format, int")
        else:
            self._transactionDatetime = transactionDatetime

    def getChargeApplied(self):
        return self._chargeApplied

    def setChargeApplied(self, chargeApplied):
        if chargeApplied is None:
            raise ValueError("Charge Applied must not be none")
        elif type(chargeApplied) != float:
            raise TypeError("Charge Applied must be a float")
        elif chargeApplied < 0:
            raise ValueError("Charge Applied must be greater than or equal to zero")
        else:
            self._chargeApplied = chargeApplied

    def getAmount(self):
        return self._amount

    def setAmount(self, amount):
        if amount is None:
            raise ValueError("Amount must not be none")
        elif type(amount) != float:
            raise TypeError("Amount must be a float")
        elif amount <= 0:
            raise ValueError("Amount must be greater than 0")
        else:
            self._amount = amount

    def getAction(self):
        return self._action

    def setAction(self, action):
        if action is None:
            raise ValueError("Action must not be none")
        elif type(action) != str:
            raise TypeError("Action must be a string")
        elif str(action).upper() != 'BUY' and str(action).upper() != 'SELL':
            raise ValueError("Action must be 'BUY' or 'SELL'")
        else:
            self._action = str(action).upper()

    def getCardNumber(self):
        return self._cardNumber

    def setCardNumber(self, cardNumber):
        isNumeric = re.compile(r'[-+]?\d+$')
        if cardNumber is None:
            raise ValueError("Card Number must not be none")
        elif type(cardNumber) != str:
            raise TypeError("Card Number must be a numeric string")
        elif len(cardNumber) != 16:
            raise ValueError("Card Number must be exactly 16 characters")

        if re.fullmatch(isNumeric, cardNumber):
            self._cardNumber = cardNumber
        else:
            raise ValueError("Card Number is invalid")

    def getExpiry(self):
        return self._expiry

    def setExpiry(self, expiry):
        if expiry is None:
            raise ValueError("Expiry must not be none")
        elif type(expiry) != str:
            raise TypeError("Expiry must be alphanumeric string")
        elif len(expiry) != 5:
            raise ValueError("Expiry must be exactly 5 characters")
        else:
            self._expiry = expiry

    def getInitialRate(self):
        return self._initialRate

    def setInitialRate(self, initialRate):
        if initialRate is None:
            raise ValueError("Initial rate must not be none")
        elif type(initialRate) != float:
            raise TypeError("Initial rate must be a float")
        elif initialRate <= 0:
            raise ValueError("Initial rate must be greater than 0")
        else:
            self._initialRate = initialRate
