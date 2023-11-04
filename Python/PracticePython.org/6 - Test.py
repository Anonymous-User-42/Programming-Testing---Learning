#   Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input("Enter a String:\n")

x = reverse(word)

if x == word:
	print("The entered string is a Palindrome")
else:
    print("The entered string is not a Palindrome")
