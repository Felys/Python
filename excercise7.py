__author__ = 'Felys'

fhand = open('mbox.txt')
print (fhand)

fhand = open('mbox.txt')
inp = fhand.read()
print (inp[:20])

str = 'this is a string'
inp = str[8:]
print(inp)

fhand = open('mbox.txt')
fread = fhand.read()
count = 0
for i in fread:
    count = count+1

print ('there is {0} characters!!'.format (count))

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('david')==-1:
        continue
    print (line)

str = 'this is a string'
str_find = str.find('s')
print(str_find)

fname = input('Enter the file name : ')
try:
    fhand = open(fname)
except:
    print('Please insert correct file name')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print ('There were', count,'subject lines in', fname)

fout = open('output.txt','w')
print (fout)
line1 = "This here's the wattle,\n"
line2 = 'the emblem of our land.\n'
line3 = "333333333333"
fout.write(line3)
fout.write(line2)
fout.close()

s = '1 2\t 3\n 4'
print(repr(s))

'''
Exercise 1   Write a program to read through a file and print the contents of the file (line by line)
all in upper case. Executing the program will look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
    BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
    SAT, 05 JAN 2008 09:14:16 -0500


You can download the file from www.py4inf.com/code/mbox-short.txt
'''
fhand = open('mbox.txt')
fread = fhand.read()

inp = input('Enter a file name:')
file_name = open(inp)
text = file_name.read()
for i in text:
    if not i.find('') == -1:
        continue
    start_index = i.find('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008')
    stop_index = i.find('Sat',start_index)
    print(i[start_index:stop_index])

elif i.find('RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>')==-1:
        continue
    elif i.find('RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])')==-1:
        continue
    elif i.find('BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA')==-1:
        continue
    elif i.find('SAT, 05 JAN 2008 09:14:16 -0500')==-1:
        continue
