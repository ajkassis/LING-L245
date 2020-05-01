import sys                                                                                                              # load frequency file
fd = open('freq.txt')

c = sys.stdin.read()
# read standard input line by line
line = sys.stdin.readline()
while line:
    print(line)
    line = sys.stdin.readline()

# tokenizing the text using split and making it variable c
line.split(' ')
# attempting to see if it exists or not and printing accordingly
# the idea here is to check the file for the words, then

if c not in 'fd':
        print(*c)
if c in 'fd':
        print(c)
