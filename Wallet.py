import hashlib

class Wallet:

    def __init__(self, name, password):
        self.current_user = name
        self.loggedin = False
        self.name = name
        self.passwordhash = self.hash_password(password)
        self.balance = 0
        self.history = []

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, name, password):
        if self.current_user == name and self.hash_password(password) == self.passwordhash:
            self.loggedin = True
            print("Login successful")
        else:
            print("Login failed")
            self.loggedin = False
        return self.loggedin

    def add_money(self, amount):
        if not self.loggedin:
            print("Please login first")
            return

        if amount > 0:
            self.balance += amount
            self.history.append(f"Added {amount}")
            print("Money added")
        else:
            print("Amount must be positive")

    def spend_money(self, amount):

        if not self.loggedin:
            print("Please login first")
            return

        if amount <= 0:
            print("Amount must be positive")

        elif amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            self.history.append(f"Spent {amount}")
            print("Money spent")

    def check_balance(self):

        if not self.loggedin:
            print("Please login first")
            return

        print(f"Balance: {self.balance}")

    def receive_money(self, amount, sender):

        if amount > 0:
            self.balance += amount
            self.history.append(f"Received {amount} from {sender}")

    def transfer_money(self, amount, receiver_wallet):

        if not self.loggedin:
            print("Please login first")
            return

        if receiver_wallet is self:
            print("Cannot send money to your own account")

        elif amount <= 0:
            print("Amount must be positive")

        elif amount > self.balance:
            print("Insufficient funds")

        else:
            self.balance -= amount
            receiver_wallet.receive_money(amount, self.name)
            self.history.append(f"Transferred {amount} to {receiver_wallet.name}")
            print("Transfer successful")

    def view_transaction_history(self):

        if not self.loggedin:
            print("Please login first")
            return

        for record in self.history:
            print(f"- {record}")