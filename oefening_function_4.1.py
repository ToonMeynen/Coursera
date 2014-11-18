hour = int(raw_input("uren die je werkt"))
rate = float(raw_input("uurloon"))


def computepay(hour, rate):
    if hour < 40:
        return hour * rate
    if hour > 40:
        overuren = hour - 40
        return 40 * rate + overuren * (rate * 1.5)
p = computepay(hour, rate)
print "Pay ", p
