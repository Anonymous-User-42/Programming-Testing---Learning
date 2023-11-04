#   Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string = input("Enter a String: ")

s = []

for c in string :
    s.append(c)
# print(s)

l = len(s)

if s[0] == s[l] :
    if s[1] == s[l-1] :
        if s[2] == s[l-2] :
            print("The entered string is a Palindrome")
        else :
            print("The entered string is not a Palindrome")
    else :
        print("The entered string is not a Palindrome")
else :
    print("The entered string is not a Palindrome")

