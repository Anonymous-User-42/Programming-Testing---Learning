#   9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#   Orignal Sample Code

#   name = input("Enter file:")
#   if len(name) < 1:
#       name = "mbox-short.txt"
#   handle = open(name)

#   Attempt #1

#   name = input("Enter file:")
#   if len(name) < 1:
#       name = "mbox-short.txt"
fh = open("mbox-short.txt")

address = dict()

for line in fh:
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        location = words[1]
        address[location] = address.get(location, 0) + 1

max = None
name = None

for key, val in address.items():
    if  max is None or val > max:
        max = val
        name = key
    else:
        continue

print(name, max)
