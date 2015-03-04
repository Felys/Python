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

str = ['z','a','b','c','d','e','f','g']
print(str[0])

fhand = open('output.txt')
count = 0
for line in fhand:
    words = line.split()
    print(words)
    if len(words) == 0 or words[0] != 'From':
        continue
    print (words[2])

str = ['z','a']
str = str.append('d')
print(str)

'''
Exercise 4   Download a copy of the file from www.py4inf.com/code/romeo.txt
Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.

For each word, check to see if the word is already in a list. If the word is not in
the list, add it to the list.

When the program completes, sort and print the resulting words in alphabetical order.
Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
'''''
file = open('mbox-short.txt')
file2 = file.read()
file3 = file2.rstrip()
print(file3)

#inp = input('Enter file: ')
file = open('romeo.txt')
word_list = []
text = file.read()
words = text.split()
for i in words:
    if i not in word_list:
        word_list.append(i)
words.sort()
print(words)


'''
Exercise 5   Write a program to read through the mail box data and when you find
line that starts with “From”, you will split the line into words using the split
function. We are interested in who sent the message which is the second word on the
From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From line and
then you will also count the number of From (not From:) lines and print out a count
at the end.

This is a good sample output with a few lines removed:
python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
'''


file = open('mbox-short.txt')
count = 0
for i in file:
    print(i)
    i = i.rstrip()
    if i.startswith('From'):
        i = i.split()
        print(i[1])
        count += 1
print('There were {0} lines in the file with From as the first word'.format(count))

'''
Exercise 6   Rewrite the program that prompts the user for a list of numbers and prints
out the maximum and minimum of the numbers at the end when the user enters “done”.
Write the program to store the numbers the user enters in a list and use the max() and min()
functions to compute the maximum and minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0
'''

list1 = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    inp = float(inp)
    list1.append(inp)
    for i in list1:
        print(i)
print(max(list1))
print(min(list1))






