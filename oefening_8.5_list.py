__author__ = 'Toon Meynen'

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)

count = 0
emails = list()

for line in fh:
    line.rstrip()
    if not line.startswith('From'):
        continue

    words = line.split()
    print words
    if words[0] == 'From':
        print words[1]
        count += 1

print "There were", count, "lines in the file with From as the first word"