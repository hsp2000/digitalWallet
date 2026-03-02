
def reverse():
    s=input("enter your statement")
    slist=list(s)
    slist = [c.lower() for c in s if c.isalpha()]
    print (slist)
    slistb=slist[::-1]
    print (slist)

    if slist==slistb:
        print("its a palindrome")
reverse()
