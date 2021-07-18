'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon = line.find(':')                          # Encuentra la posicion (el index) del caracter :
    count = count + 1
    #print(line.rstrip())
    #line = line.rstrip()                           # Elimina la linea en blanco entre cada output
    #print(line[colon + 2: ])
    x = float(line[colon + 2: ])                    # Convierte la cadena que va desde la posicion de (colon + 2)
                                                    # hasta el final, en una variable tipo float
    total = total + x
    ave = total / count
#print("Done: ", count, 'lines')
#print(colon)
print('Average spam confidence:', ave)
