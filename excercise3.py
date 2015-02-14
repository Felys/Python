x = 3
y = 10

if x == y:
    print('X and Y are equal')
else:
    if x > y:
        print('X is greater than Y')
    else:
        print('X is less than Y')


###############################################

hours = input('Enter hours : ')
rate = input('Enter rate : ')
if float(hours) > 40:
    pay = float(hours) * float(rate) * 1.5
else:
    pay = float(hours) * float(rate)
print('Pay : ' + str(pay))

# Exercise 2   Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:Enter Hours: 20
#Enter Rate: nine
#Enter Hours: forty
#Error, please enter numeric input

hours = input('Enter Hours')
rate = input('Enter Rate')
pay = float(hours) * float(rate)
overtime_pay = float(hours) * float(rate) * 1.5

try:
    if float(hours) > 40:
        print('Pay : ', overtime_pay)
    else:
        print('Pay : ', pay)

except:
    print('Please enter a number')

hours = input('Enter Hours')
rate = input('Enter Rate')
pay = float(hours) * float(rate)
overtime_pay = float(hours) * float(rate) * 1.5

try:
    if float(hours) > 40:
        print('Pay : {0}'.format(overtime_pay))
    else:
        print('Pay : {0}'.format(pay))

except:
    print('Please enter a number')

'''Exercise 3   Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F

Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
'''
score = input('Please insert score')
try:
    if float(score) <= 1.0 and float(score) >= 0.9:
        print('A')
    elif float(score) < 0.9 and float(score) >= 0.8:
        print('B')
    elif float(score) < 0.8 and float(score) >= 0.7:
        print('C')
    elif float(score) < 0.7 and float(score) >= 0.6:
        print('D')
    elif float(score) < 0.6:
        print('F')
    elif float(score) > 1.0:
        print('Bad Score')
except:
    print('Bad Score')




