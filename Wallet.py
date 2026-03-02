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
        if sender== self.name:
            print("cannot send money to your own account")
        else:
                if amount>0:
                    self.balance += amount
                    self.history.append(f"Received {amount} from {sender}")
                else:
                    print("an error has occured.transaction cancelled")

    def transfer_money(self, amount, receiver_wallet):
        if receiver_wallet== self.name:
            print("cannot send money to your own account")
        else:
            if amount <= 0:
                print("Amount must be positive")
            elif amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                receiver_wallet.receive_money(amount, self.name)
                self.history.append(f"Transferred {amount} to {receiver_wallet.name}")
                print("Transfer successful")

    def view_transaction_history(self):
        for record in self.history:
            print(f"- {record}")
     