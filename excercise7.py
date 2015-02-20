__author__ = 'Felys'

fhand = open('mbox-short.txt')
for i in fhand:
    i = i.rstrip()
    if not i.startswith('From:'):
        continue
    print(i)

fhand = open('mbox-short.txt')
for i in fhand:
    i = i.rstrip().upper()
    print (i)

fhand = open('mbox-short.txt')
sum = 0
count = 0
for i in fhand:
    i = i.rstrip()
    if i.startswith('X-DSPAM-Confidence:'):
        value = float((i[20:26]))
        sum = sum+value
        count = count+1
        avg = sum/count
print(avg)

fhand = open('mbox-short.txt')
for i in fhand:
    i = i.rstrip()
    if i.find('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'):
        print (i)


increment = 1
total = 0
while increment < 3 :
    increment = increment+1
    print('this is increment {0}'.format(increment))
    total = increment+total
    print('this is total {0}'.format(total))

print(total)


