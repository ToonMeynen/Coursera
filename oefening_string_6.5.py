text = "X-DSPAM-Confidence:    0.8475"
start_pos = text.find(':')
sub_str = text[start_pos+1:]
sub_str = str.strip(sub_str)
float_num = float(sub_str)
print str.strip(sub_str)



