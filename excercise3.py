x = 3
y = 10

if x == y :
    print ('X and Y are equal')
else :
    if x > y :
        print ('X is greater than Y')
    else :
        print ('X is less than Y')


###############################################

hours = input('Enter hours : ')
rate = input('Enter rate : ')
if float(hours) > 40 :
    pay = float(hours) * float(rate) * 1.5
else :
    pay = float(hours) * float(rate)
print('Pay : '+str(pay))

#Exercise 2   Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:Enter Hours: 20
#Enter Rate: nine
#Enter Hours: forty
#Error, please enter numeric input

hours = input('Enter Hours')
rate = input('Enter Rate')
pay = float(hours) * float(rate)
overtime_pay = float(hours) * float(rate)* 1.5

try:
    if float(hours) > 40 :
        print ('Pay : ', overtime_pay)
    else :
        print ('Pay : ', pay)

except:
    print ('Please enter a number')


hours = input('Enter Hours')
rate = input('Enter Rate')
pay = float(hours) * float(rate)
overtime_pay = float(hours) * float(rate)* 1.5

try:
    if float(hours) > 40 :
        print ('Pay : {0}'.format(overtime_pay))
    else :
        print ('Pay : {0}'.format(pay))

except:
    print ('Please enter a number')


