from Wallet import Wallet
from WalletManager import WalletManager

manager = WalletManager()

while True:
    print("\n--- Wallet System Menu ---")
    print("1. Create Wallet")
    print("2. Add Money")
    print("3. Spend Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Show All Wallets")
    print("7. show transaction history")
    print("8. exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        manager.create_wallet(name)

    elif choice == "2":
        name = input("Enter your name: ")
        amount = int(input("Amount: "))
        manager.add_money(name, amount)

    elif choice == "3":
        name = input("Enter your name: ")
        amount = int(input("Amount: "))
        manager.spend_money(name, amount)

    elif choice == "4":
        sender = input("Your name: ")
        receiver = input("Send to: ")
        amount = int(input("Amount: "))
        manager.transfer_money(sender, receiver, amount)

    elif choice == "5":
        name = input("Enter your name: ")
        manager.check_balance(name)

    elif choice == "6":
        manager.output_data()

    elif choice == "7":
        name= input("your name?")
        manager.view_transaction_history(name)

    elif choice == "8":
        print("Exiting system...")
        break
    else:
        print("Invalid option")