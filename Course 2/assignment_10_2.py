'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()

# Create a list of all the hours
for line in handle:
    if line.startswith('From ') == True:
        line = line.rstrip()
        x = line.split()
        time = x[5]
        hour = time.split(':')
        hrs = hour[0]
        #print(hrs)
        lst.append(hrs)

# Make the histogram
for hr in lst:
    counts[hr] = counts.get(hr, 0) + 1

#print(lst)
#print('\n', counts)
sort_counts = sorted(counts.items())           # Sort the histogram and at the same time create a list of tuples
#print(sort_counts)
for k, v in sort_counts:              # Print key and value which in this case is the hour and number of times it is repeated.
    print(k, v)
