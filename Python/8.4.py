#   Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

#   You can download the sample data at http://www.py4e.com/code3/romeo.txt

#   Orignal Sample Code

#   fname = input("Enter file name: ")
#   fh = open(fname)
#   lst = list()
#   for line in fh:
#       print(line.rstrip())

#   Attempt #1

#   fname = input("Enter file name: ")
#   fh = open(fname)
#   fh = open("romeo.txt")
#   lst = list()
#   for words in fh:
#       word = words.strip()
#       if word not in lst:
#           lst = lst.append(word)
#       else:
#           continue
#
#   srt = lst.sort()
#
#   print(srt)

#   Attempt #2

fh = open("romeo.txt")
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)

lst.sort()

print(lst)
