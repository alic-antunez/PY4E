'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
name = input("Enter file:")

# This means that if you hit Enter on the pront called 'Enter File' (you have lenght less than 1, you have zero),
# If length is zero then name = "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)              # Open the file
sender = dict()              # Create an empty dictionary
list = []                    # Create an empty list

# Build the list
for line in fh:              # A loop for to find any line starting with From
    if line.startswith('From ') == True:
        line = line.strip()       # Eliminate the line jump
        x = line.split()          # Convert the line on a list
        y = x[1]                  # Second word of the list
        list.append(y)            # Add up the second word to my list

# build the histogram
for i in list:
    sender[i] = sender.get(i, 0) + 1         # For every value in "list"  add the new item
print(sender)

# Who is the winner?
bigcount = None
bigmail = None
for mail,num in sender.items():
    if bigcount is None or num > bigcount:
        bigcount = num
        bigmail = mail
print(bigmail, bigcount)
