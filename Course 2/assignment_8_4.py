'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order

El texto es romeo.txt
But soft what light through yonder window breaks.
It is the east and Juliet is the sun Arise
fair sun and kill the envious moon
Who is already sick and pale with grief
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line.rstrip())
    split = line.split()
    for i in split:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
