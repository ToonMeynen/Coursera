largest = None
smallest = None
num = None

while True:
    user_input = raw_input("Enter a number: ")
    if user_input == "done":
        break
    try:
        num = int(user_input)
    except Exception, e:
        print 'Invalid input'
        continue

    if num > largest:
        largest = num

    if smallest is not None:
        if num < smallest:
            smallest = num
    else:
        smallest = num
        
print "Maximum is", largest
print "Minimum is", smallest