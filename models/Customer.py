class Customer:

    def __init__(self, customerID=None, passwordHash=None, registerDatetime = None, emailAddress=None,
                 previousSignInDatetime=None, currentSignInDatetime=None, name=None):
        # self.__customerID = Customer.generateNewCustomerID()
        # self.setCustomerID(customerID)
        self.__customerID = customerID
        self.__passwordHash = passwordHash
        self.__registerDatetime = registerDatetime
        self.__emailAddress = emailAddress
        self.__previousSignInDatetime = previousSignInDatetime
        self.__currentSignInDatetime = currentSignInDatetime
        self.__name = name

    def getCustomerID(self):
        return self.__customerID

    def setCustomerID(self, customerID):
        if customerID is None:
            raise ValueError("Customer ID must not be none")
        elif type(customerID) != str:
            raise TypeError("Customer ID must be alphanumeric string")
        elif len(customerID) != 20:
            raise ValueError("Customer ID must be exactly 20 characters")
        # If no customer ID exists (could be a new customer) then generate one and set it
        else:
            self.__customerID = customerID

        # raise ValueError("Customer ID must not be set to None")

    def getPasswordHash(self):
        return self.__passwordHash

    def setPasswordHash(self, passwordHash):
        if passwordHash is None:
            raise ValueError("Password hash must not be none")
        elif type(passwordHash) != str:
            raise TypeError("Password hash must be a string")
        elif len(passwordHash) != 60:
            raise ValueError("Password hash must be 60 characters")
        else:
            self.__passwordHash = passwordHash

    def getRegisterDatetime(self):
        return self.__registerDatetime

    def setRegisterDatetime(self, registerDatetime):
        if registerDatetime is None:
            raise ValueError("Register datetime must not be none")

    def getEmailAddress(self):
        return self.__emailAddress

    def setEmailAddress(self):
        pass

    def getPreviousSignInDatetime(self):
        return self.__previousSignInDatetime

    def setPreviousSignInDatetime(self):
        pass

    def getCurrentSignInDatetime(self):
        return self.__currentSignInDatetime

    def setCurrentSignInDatetime(self):
        pass

    def getName(self):
        return self.__name

    def setName(self):
        pass







