__author__ = 'toon'
fname = raw_input('enter the filename')
if len(fname) < 1:
    fname = 'words.txt'
fhand = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
print "Done"









