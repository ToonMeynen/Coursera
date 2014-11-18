#geef een rate bij een bepaalde score.
try:
    rate = float(raw_input('enter a rate between 0.0 - 1.0 : '))
except:
    print 'please enter a valid rate'
    exit()
if rate > 0.0 and rate <= 1.0:
    if rate >= 0.9:
        print 'A'
    elif rate >= 0.8:
        print 'B'
    elif rate >= 0.7:
        print 'C'
    elif rate >= 0.6:
        print 'D'
    elif rate < 0.6:
        print 'F'
else:
    print 'enter a valid value rate'
