__author__ = 'Toon Meynen'

fh = open('mbox-short.txt')

emails = list()

for line in fh:
    line.rstrip()
    if not line.startswith('From'):
        continue
    chopped = line.split()
    emails.append(chopped[1])

for email in emails:
    print email

count = len(emails)

print "There were", count, "lines in the file with From as the first word"

