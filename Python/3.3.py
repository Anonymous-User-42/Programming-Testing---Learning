a = 0.5

score = input("Enter Score: ")

s = float(score)

if s >= 0.0 :
    a = 1.0
else :
    print("Error: Out of Range")

if s <= 1.0 :
    a = 0.0
else :
    print("Error: Out of Range")

if a == 0.0 :
    if s >= 0.9 :
        print("A")
    elif s >= 0.8 :
        print("B")
    elif s >= 0.7 :
        print("C")
    elif s >= 0.6 :
        print("D")
    elif s > 0.6 :
        print("F")
