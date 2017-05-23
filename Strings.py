text = "X-DSPAM-Confidence:    0.8475";
position = text.find('0')
finalValue = float(text[position:])

print finalValue