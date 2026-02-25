wallet={}

def createWallet():
    x=input("enter your first name to create a digital wallet:")
    if x in wallet:
        print(" there is already a wallet under your name, you do not need to crate another.")
    else:
        wallet[x]={"balance":0 ,"history":[]}
        print("your wallet has been created.")
        print(wallet)

def addMoney():
    name=input("enter your name:")
    try:
        money=int(input("enter the amount"))
        if money>=0:
            if name in wallet:
                wallet[name]["balance"] += money
                wallet[name]["history"].append("added "+str(money))
            else:
                print("a wallet under the given name deosnt exist")
        else:
            print("you cannot have a negative balance")

    except ValueError:
        print("please enter a valid number for amount.")
        
    
def spendMoney():
    name=input("enter your name:")
    try:
        money=int(input("enter the amount to be spent"))

        if name in wallet:
            if money<=wallet[name]["balance"]:
                wallet[name]["balance"]=wallet[name]["balance"]-money
                wallet[name]["history"].append("spent: "+str(money))
            else:
                print(" you do not have enough money to complete this purchase")
        else:
            print("a wallet under the given name deosnt exist")

    except ValueError:
        print("please enter a valid number for amount.")
        

def checkBalance():
    name=input("enter your name:")
    if name in wallet:
        print("the amount in your wallet is: "+str(wallet[name]["balance"]))
    else:
        print("a wallet under the given name deosnt exist") 

def transferMoney():
        you=input("enter your name:")
        them= input("enter the name of the account you want to transfer to:")
        if you != them:
            if you in wallet and them in wallet:
                try:
                    money=int(input("enter the amount to be transferred :"))
                    if money <= 0:
                        print("transfer cannot be completed due negative amounts")
                    else:
                        if wallet[you]["balance"]<money :
                            print("transfer cannot be completed due insufficient funds")
                        else:
                            wallet[you]["balance"]=wallet[you]["balance"]-money
                            wallet[you]["history"].append("transferred money: " +str(money))
                            wallet[them]["balance"]=wallet[them]["balance"]+money 
                            wallet[them]["history"].append("received money: " +str(money)) 
                except ValueError:
                     print("please enter a valid number for amount.")     

            else:
                print("transfer cannot be completed due inaccurate names of the accounts")
        else:
            print("cannot transfer money to the same account")
            return       
        print(wallet)

while True:
    print("\n1. Create Wallet")
    print("2. Add Money")
    print("3. Spend Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        createWallet()
    elif choice == "2":
        addMoney()
    elif choice == "3":
        spendMoney()
    elif choice == "4":
        transferMoney()
    elif choice == "5":
        checkBalance()
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid option, try again") 
