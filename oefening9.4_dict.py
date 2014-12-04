__author__ = 'toon'

email_dict = dict()
max_email = None
max_count = None

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith("From"):
        continue
    email_line = line.rstrip().split()
    email = email_line[1]
    if email_line[0] == "From":
        email_dict[email] = email_dict.get(email, 0) + 1

for email, count in email_dict.items():
    if max_count is None or count > max_count:
        max_count = count
        max_email = email
print max_email, max_count

