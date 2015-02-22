__author__ = 'Felys'

names = ['Anand','Bob']
for i in names:
    print(i)
    if i.find('A') != -1:
        print ('Anand starts with a vowel')
    else:
        print('Not start with a vowel')

names = ['Bob','Anand','Rick','Unity']
for name in names:
    if name[0] in 'AEIOU':
        print ('{0} this one has a vowel'.format(name))

list_a = [1,'EE',['FF','GG'],4]
print (list_a[0,4])

'EE' in list_a

for i in list_a:
    print(i)

list2 = [1]
list = [2,3,4]
for i in range(len(list)):
    list[i] = list[i] *2
print (list)

listA = [1,2,3]
listB = [4,5,6]
print(listA * 3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[0:1] = [1,2]
print (t[0:2])

t = ['a', 'b', 'c', 'd', 'e', 'f']
t.append('a')
t.extend(listA)
x = t.pop(5)
print (x)
print (t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
f = t.remove('f')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[0]
print(t)

numlist = list()
while (True):
    inp = input('insert coin[s] : ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
avg = sum(numlist)/len(numlist)
print (avg)

s = 'this is a string'
t = list(s)
ssplit = s.split()
print (ssplit)
delimiter = ' '
sjoin = delimiter.join(ssplit)
print(sjoin)

fhand = open(('mbox-short.txt'))
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print (len(words))

a = 'ba'
b = 'ba'
a is b

#
def delete_first(t):
    del t[0]

letter = ['a','b','c']
delete_first(letter)
print(letter)

letter = [1,2,3]
letter2 = letter[1:]
print(letter)

'''
Exercise 1
Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list that contains all but the first and last
elements.
'''

str = ['a','b','c','d','e','f','g']

def chop(list):
    del list[0],list[-1]
    return None

str = ['a','b','c','d','e','f','g']
strchop = chop(str)
print(str)
print(strmiddle)


def middle(list):
    list = list[1:-1]
    return list

str = ['a','b','c','d','e','f','g']
strmiddle = middle(str)
print(str)
print(strmiddle)

str2 =['z','d','a']
str2.sort()
print(str2)


str = ['z','a','b','c','d','e','f','g']
str.sort()
print(str)

fhand = open('output.txt')
count = 0
for line in fhand:
    words = line.split()
    print(words)
    if len(words) == 0 or words[0] != 'From':
        continue
    print (words[2])







