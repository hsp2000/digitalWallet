from Wallet import Wallet

wallets = {}

while True:
    print("\n1. Create Wallet")
    print("2. Add Money")
    print("3. Spend Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        if name in wallets:
            print("Wallet already exists")
        else:
            wallets[name] = Wallet(name)
            print("Wallet created")

    elif choice == "2":
        name = input("Enter your name: ")
        if name in wallets:
            amount = int(input("Amount: "))
            wallets[name].add_money(amount)
        else:
            print("Wallet not found")

    elif choice == "3":
        name = input("Enter your name: ")
        if name in wallets:
            amount = int(input("Amount: "))
            wallets[name].spend_money(amount)
        else:
            print("Wallet not found")

    elif choice == "4":
        sender = input("Your name: ")
        receiver = input("Send to: ")

        if sender in wallets and receiver in wallets:
            amount = int(input("Amount: "))
            wallets[sender].transfer_money(amount, wallets[receiver])
        else:
            print("Wallet not found")

    elif choice == "5":
        name = input("Enter your name: ")
        if name in wallets:
            wallets[name].check_balance()
        else:
            print("Wallet not found")

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid option")