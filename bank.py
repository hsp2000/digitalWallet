from Wallet import Wallet
from WalletManager import WalletManager

manager = WalletManager()

# ---- LOGIN OR CREATE WALLET ----
while True:
    print("\n--- Welcome to the Wallet System ---")
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if manager.wallet_exists(name):
        if manager.login(name, password):
            print(f"Login successful! Welcome back, {name}.")
            current_wallet = manager.wallets[name]
            break
        else:
            print("Incorrect password. Try again.")
    else:
        manager.create_wallet(name, password)
        print(f"Wallet created for {name}. Please log in again.")

# ---- MAIN MENU LOOP ----
while current_wallet.loggedin:
    print("\n--- Wallet Menu ---")
    print("1. Add Money")
    print("2. Spend Money")
    print("3. Transfer Money")
    print("4. Check Balance")
    print("5. Show All Wallets")
    print("6. Show Transaction History")
    print("7. Logout / Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Amount to add: "))
            current_wallet.add_money(amount)
        except ValueError:
            print("Invalid amount. Enter a number.")

    elif choice == "2":
        try:
            amount = float(input("Amount to spend: "))
            current_wallet.spend_money(amount)
        except ValueError:
            print("Invalid amount. Enter a number.")

    elif choice == "3":
        receiver_name = input("Send money to (name): ")
        if not manager.wallet_exists(receiver_name):
            print("Receiver wallet not found.")
            continue
        receiver_wallet = manager.wallets[receiver_name]
        try:
            amount = float(input("Amount to transfer: "))
            current_wallet.transfer_money(amount, receiver_wallet)
        except ValueError:
            print("Invalid amount. Enter a number.")

    elif choice == "4":
        current_wallet.check_balance()

    elif choice == "5":
        print(manager.wallets)

    elif choice == "6":
        current_wallet.view_transaction_history()

    elif choice == "7":
        current_wallet.logout()
        print("You have logged out. Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-7.")