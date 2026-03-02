from Wallet import Wallet

class WalletManager:
    def __init__(self):
        self.wallets = {}

    def output_data(self):
        if not self.wallets:
            print("No wallets available")
        else:
            for name, wallet in self.wallets.items():
                print(f"{name}: Balance = {wallet.balance}")

    def wallet_exists(self, name):
        return name in self.wallets

    def create_wallet(self, name):
        if not self.wallet_exists(name):
            self.wallets[name] = Wallet(name)
            print(f"Wallet for {name} created")
        else:
            print("Wallet already exists")

    def add_money(self, name, amount):
        if self.wallet_exists(name):
            self.wallets[name].add_money(amount)
        else:
            print("Wallet not found")

    def spend_money(self, name, amount):
        if self.wallet_exists(name):
            self.wallets[name].spend_money(amount)
        else:
            print("Wallet not found")

    def transfer_money(self, sender, receiver, amount):
        if self.wallet_exists(sender) and self.wallet_exists(receiver):
            self.wallets[sender].transfer_money(amount, self.wallets[receiver])
        else:
            print("Sender or receiver wallet not found")

    def check_balance(self, name):
        if self.wallet_exists(name):
            self.wallets[name].check_balance()
        else:
            print("Wallet not found")

    def view_transaction_history(self,name):
        wallet = self.wallets[name]
        if wallet.history:
            self.wallets[name].view_transaction_history()
        else:
            print("Wallet not found")