__author__ = 'toon'
fname = raw_input('enter the filename')
if len(fname) < 1:
    fname = 'words.txt'
fhand = open(fname)
for line in fhand:
    line = line.rstrip().upper()
    print line







