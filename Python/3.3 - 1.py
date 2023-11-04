#score = input("Enter Score: ")

#s = float(score)

from numpy import void0


s = float(input("Enter Score: "))

def z(s) :
    if s >= 0.9 :
        return("A")
    elif s >= 0.8 :
        return("B")
    elif s >= 0.7 :
        return("C")
    elif s >= 0.6 :
        return("D")
    else : # s < 0.6 :
        return("F")
#    return s

if s >= 0.0 :
    if s <= 1.0 :
        print(z(s))
    else :
        print("Error: Out of Range")
else :
    print("Error: Out of Range")




