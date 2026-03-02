
print("hellooo world")

#You’re counting people collecting coins.
coinsList={}

def collect (name):
        if name in coinsList:
            if coinsList[name]>=10:
                print(" maximum coins that a person can have is 10")
                return False
            else:
                value=coinsList[name]+1
                coinsList[name]=value
                return True
        else:
            coinsList[name]=1
            return True
    #print (coinsList)

# def resetbell(name):
#     if name in doorbellrings:
#         doorbellrings[name]=0
#         print("doorbell has been rsset")
#     else:
#         print(name + "has not rung  the bell")

for i in range(11):
    collect("Himaya")

collect("Hasee")
collect("Yasara")



if collect("hi"):

    print(coinsList)
