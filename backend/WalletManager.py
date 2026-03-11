from Wallet import Wallet

class WalletManager:

    def __init__(self):
        self.wallets = {}

    def wallet_exists(self, name):
        return name in self.wallets

    def create_wallet(self, name, password):

        if not self.wallet_exists(name):
            self.wallets[name] = Wallet(name, password)
            print(f"Wallet for {name} created")

        else:
            print("Wallet already exists")

    def login(self, name, password):

        if self.wallet_exists(name):
            return self.wallets[name].authenticate(name, password)

        print("Wallet not found")
        return False