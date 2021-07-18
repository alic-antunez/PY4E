'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''

score = input('Enter Score: ')
try:
    fscore = float(score)
except:
    print('Please, enter a numeric input')
    quit()

if fscore < 0 or fscore > 1:
    print('Your grade is out of range. Please specify a numeric input between 0.0 and 1.0')
elif fscore >= 0.9:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    print('D')
elif fscore < 0.6:
    print('F')
elif fscore < 0 or fscore > 1:
    print('Your grade is out of range. Please specify a numeric input between 0.0 and 1.0')
