
print("hellooo world")

#You’re counting how many times someone rings a doorbell.
doorbellrings={}

def ringBell (name):
        if name in doorbellrings:
            if doorbellrings[name]>=3:
                print(name+"has rung the bell too many times, the bell has now been disabled.")
                return False
            else:
                value=doorbellrings[name]+1
                doorbellrings[name]=value
                return True
        else:
            doorbellrings[name]=1
            return True
    #print (doorbellrings)

def resetbell(name):
    if name in doorbellrings:
        doorbellrings[name]=0
        print("doorbell has been rsset")
    else:
        print(name + "has not rung  the bell")

ringBell("Himaya")
ringBell("Himaya")
ringBell("Himaya")
resetbell("Himaya")
ringBell("Hasee")
ringBell("Yasara")

if ringBell("hi"):

    print(doorbellrings)
