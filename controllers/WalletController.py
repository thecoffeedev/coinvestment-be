from data_access.WalletDataAccess import WalletDataAccess


class WalletController:

    def __init__(self, app):
        self.daWallet = WalletDataAccess(app)


    def createWallet(self):
        self.daWallet.createWallet()
        print("in wallet controller")
