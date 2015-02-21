__author__ = 'Felys'

fhand = open('mbox.txt')
print (fhand)

fhand = open('mbox.txt')
user_input = fhand.read()
print (user_input[:20])

str = 'this is a string'
user_input = str[8:]
print(user_input)

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

user_input = input('Enter a file name:')
file_name = open(user_input)
for i in file_name:
    i = i.rstrip().upper()
    print(i)

'''
Exercise 2   Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence:  0.8475


When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating point number
 on the line. Count these lines and the compute the total of the spam confidence values from these lines. When you reach
  the end of the file, print out the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519


Test your file on the mbox.txt and mbox-short.txt files.
'''

user_input = input('Enter the file name')
file_handler = open(user_input)
total = 0
count = 0
for i in file_handler:
    i = i.rstrip()
    if i.startswith('X-DSPAM-Confidence:'):
        i = i[20:]
        i = float(i)
        total = i + total
        count = count + 1
avg = total/count
print('Average spam confidence: {0}'.format(avg))

'''
 Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the
  exact file name ’na na boo boo’. The program should behave normally for all other files which exist and don’t exist.
  Here is a sample execution of the program:python egg.py

Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
'''

user_input = input('Enter the file name: ')
try:
    line = 0
    file = open(user_input)
    for i in file:
        if i.startswith('Subject:'):
            line = line + 1
    print('There were {0} subject lines in {1}'.format(line,user_input))
except:
    if user_input == ('na na boo boo'):
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened: {0}'.format(user_input))


