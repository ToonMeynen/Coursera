hour = int(raw_input("uren die je werkt"))
rate = float(raw_input("uurloon"))

if hour < 40:
    bruto_loon = hour * rate
if hour > 40:
    overuren = hour - 40
    bruto_loon = 40 * rate + overuren * (rate * 1.5)
print bruto_loon