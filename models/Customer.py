import re

class Customer:

    def __init__(self, customerID=None, passwordHash=None, registerDatetime = None,
                 emailAddress=None, previousSignInDatetime=None, currentSignInDatetime=None,
                 name=None):
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
            raise TypeError("Customer ID must not be none")
        elif type(customerID) != str:
            raise TypeError("Customer ID must be alphanumeric string")
        elif len(str(customerID).strip()) != 20:
            raise ValueError("Customer ID must be exactly 20 characters")
        else:
            self.__customerID = customerID

    def getPasswordHash(self):
        return self.__passwordHash

    def setPasswordHash(self, passwordHash):
        if passwordHash is None:
            raise TypeError("Password hash must not be none")
        elif type(passwordHash) != str:
            raise TypeError("Password hash must be a string")
        elif len(str(passwordHash).strip()) != 60:
            raise ValueError("Password hash must be 60 characters")
        else:
            self.__passwordHash = passwordHash

    def getRegisterDatetime(self):
        return self.__registerDatetime

    def setRegisterDatetime(self, registerDatetime):
        if registerDatetime is None:
            raise TypeError("Register datetime must not be none")
        elif type(registerDatetime) != int:
            raise TypeError("Time must be in unix time format, int")
        else:
            self.__registerDatetime = registerDatetime

    def getEmailAddress(self):
        return self.__emailAddress

    def setEmailAddress(self, emailAddress):
        emailPattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if emailAddress is None:
            raise TypeError("Email address must not be none")
        elif type(emailAddress) != str:
            raise TypeError("Email address must be a string")

        if re.fullmatch(emailPattern, emailAddress):
            self.__emailAddress = emailAddress
        else:
            raise ValueError("Email address entered is not valid")

    def getPreviousSignInDatetime(self):
        return self.__previousSignInDatetime

    def setPreviousSignInDatetime(self, previousSignInDatetime):
        if previousSignInDatetime is None:
            raise TypeError("Register datetime must not be none")
        elif type(previousSignInDatetime) != int:
            raise TypeError("Time must be in unix time format, int")
        else:
            self.__previousSignInDatetime = previousSignInDatetime

    def getCurrentSignInDatetime(self):
        return self.__currentSignInDatetime

    def setCurrentSignInDatetime(self, currentSignInDatetime):
        if currentSignInDatetime is None:
            raise TypeError("Register datetime must not be none")
        elif type(currentSignInDatetime) != int:
            raise TypeError("Time must be in unix time format, int")
        else:
            self.__currentSignInDatetime = currentSignInDatetime

    def getName(self):
        return self.__name

    def setName(self, name):
        if name is None:
            raise TypeError("Register datetime must not be none")
        elif type(name) != str:
            raise TypeError("Name must be a string")
        elif len(str(name).strip()) < 2:
            raise ValueError("Name must be more than two characters")
        else:
            self.__name = name
