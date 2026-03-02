class Wallet:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Added {amount}")
            print("Money added")
        else:
            print("Amount must be positive")

    def spend_money(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.history.append(f"Spent {amount}")
            print("Money spent")

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def receive_money(self, amount, sender):
        self.balance += amount
        self.history.append(f"Received {amount} from {sender}")

    def transfer_money(self, amount, receiver_wallet):
        if amount <= 0:
            print("Amount must be positive")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            receiver_wallet.receive_money(amount, self.name)
            self.history.append(f"Transferred {amount} to {receiver_wallet.name}")
            print("Transfer successful")