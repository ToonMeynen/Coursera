__author__ = 'toon'
fname = raw_input('enter the filename')
if len(fname) < 1:
    fname = 'words.txt'
fh = open(fname)

total_sum = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    line.rstrip()
    sp = line.find(':')
    num = float(line[sp+2:-1])
    total_sum += num
avr = total_sum / count
print "Average spam confidence:", avr









