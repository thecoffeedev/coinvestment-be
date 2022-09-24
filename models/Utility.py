import random
import string
from passlib.hash import bcrypt
import time


class Utility:

    @staticmethod
    def generatePasswordHash(password):
        # 72 max length
        # 8 minimum length, alphanumeric and special characters
        if password is None:
            raise ValueError("Password must not be none")
        elif type(password) != str:
            raise TypeError("Password must be a string")

        if len(password) < 8 or len(password) > 72:
            raise ValueError("Password must be between 8 and 72 characters")

        return bcrypt.hash(password)

    # Returns True if the password is verified
    @staticmethod
    def verifyPassword(password, passwordHash):
        if password is None or passwordHash is None:
            raise ValueError("Password must not be none")
        elif type(password) != str:
            raise TypeError("Password must be a string")
        elif type(passwordHash) != str:
            raise TypeError("Password hash must be a string")
        elif len(str(password).strip()) < 8 or len(str(password).strip()) > 72:
            raise ValueError("Password must be between 8 and 72 characters")
        elif len(passwordHash) != 60:
            raise ValueError("Password has must be 60 characters")

        return bcrypt.verify(password, passwordHash)

    @staticmethod
    def generateRandomID():
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for i in range(20))

    @staticmethod
    def unixTimestampToString(unixTimestamp):
        #return time.time()
        pass