#   Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

#   X-DSPAM-Confidence:    0.8475

#   Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

#   You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

count = 0
num_s = 0    #    "s" stands for Sum

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    start = line.find(":")    #   ":" in the "X-DSPAM-Confidence:"
    string = line[start + 1 : ]    #    String Slicing to process just int()
    string = string.strip()    #    String Striping to strip whitespaces to obtain int() in str() form purely
    num = float(string)    #    Conversion of str() to float() to process numbers
    num_s = num_s + num    #    Summing up the processed numbers in for loop
print("Average spam confidence:", num_s / count)    #    Printing the Average with String context

