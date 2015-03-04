__author__ = 'Felys'

eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp = {'two':'dos','three':'tres'}
print(eng2sp)
print(eng2sp['four'])

'''Exercise 1
Write a program that reads the words in words.txt and stores them
as keys in a dictionary. It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether
a string is in the dictionary.
'''

fhand = open('word.txt')
store = dict()
text = fhand.read()
words = text.split()
for i in words:
    store[i] = None

'From' in store

###########################

word = 'bronto'
d = dict()
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i]+1
print (d)

d = dict()
d['1'] = 'one'
print(d)

counts = {'a':1,'b':2}
print(counts.get('a',0))

word = 'abc'
d = dict()
for i in word:
    d[i] = d.get(i)
    print(i)
print (d)


word = 'bronto'
d = dict()
for i in word:
    if i not in d:
        d[i] = 1
    elif i in d:
        d[i] = d[i]+1
print (d)

word = 'bronto'
d = dict()
for i in word:
    d[i] = d.get(i,0)
print(d)

try:
    fhand = open('romeo.txt')
except:
    print('romeo cannot be opened')
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for i in words:
        counts[i] = counts.get(i,0)+1

print(counts)


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for i in counts:
    print(i,counts[i])

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = counts.keys()
#lst_sort = sorted(lst)
#print(lst_sort)
for i in sorted(lst):
    print (i, counts[i])

import string
try:
    fhand = open('romeo2.txt')
except:
    print('romeo cannot be opened')
    exit()
#counts = dict()
for line in fhand:
    for i in string.punctuation:
        i = i.replace(i,'')
    print(line)

import string
s = open('romeo2.txt')
s2 = s.read()
for c in string.punctuation:
    s2 = s2.replace(c,"")
print(s2)
'''
Exercise 2   Write a program that categorizes each mail message by which
day of the week the commit was done. To do this look for lines which start
with “From”, then look for the third word and then keep a running count of
each of the days of the week. At the end of the program print out the
contents of your dictionary (order does not matter).Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
'''

fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    line = line.strip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        day = words[2]
        counts[day] = counts.get(day,0)
        if day in counts:
            counts[day] = counts[day]+1
print (counts)

fhand = open('mbox-short.txt')
counts = {'Mon':0,'Tue':0,'Wed':0,'Thu':0,'Fri':0,'Sat':0,'Sun':0}
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        words = line.split()
        print(words)
        for word in words:
            if word in counts:
                counts[word] = counts[word]+1
print (counts)

'''
Exercise 3   Write a program to read through a mail log, and build a histogram
using a dictionary to count how many messages have come from each email
address and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
'''

fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email,0)+1
print(counts)

'''Exercise 4   Add code to the above program to figure out who has the most
messages in the file.
After all the data has been read and the dictionary has been created,
look through the dictionary using a maximum loop (see Section ??)
to find who has the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''''
#count email
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email,0)+1
#find maximum
largest = 0
for i in counts:
    email_val = counts.get(i)
    if largest < email_val:
        largest = email_val
#map maximum value with key
max_email = None
for i in counts:
    if counts.get(i) == largest:
        max_email = i
#finally...
print('{0} {1}'.format(max_email,largest))
#alternative way to find value,key
for name,age in counts.items():
    if age == largest:
        print (name)

'''
Exercise 5   This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from
(i.e. the whole e-mail address). At the end of the program print out the
contents of your dictionary. python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

fhand = open('mbox-short.txt')
counts = {}
for line in fhand:
    if line.startswith('From:'):
       line = line.strip()
       atpos = line.find('@')
       domain = line[atpos+1:]
       counts[domain] = counts.get(domain,0)+1
print(counts)





