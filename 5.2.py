# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

#   The below program has finite limits for its inputs

largest = -999999999999999999999999999999999999999999999999999999
smallest = 999999999999999999999999999999999999999999999999999999
while True:
    num = input("Enter a number: ")
    try :
        #   n = float(num)
        n = int(num)
    except :
        if num != "done" :
            #   print("Input is not Valid")
            print("Invalid input")
    if n > largest :
        largest = n
    elif n < smallest :
        smallest = n       
    if num == "done" :
        break
    else :
        continue
    #   print(n)
    

print("Maximum is", largest)
print("Minimum is", smallest)


# for i in n :
#     if n >>= :
# 
# 

