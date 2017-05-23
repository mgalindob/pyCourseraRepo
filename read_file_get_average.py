    # Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fname = "Data/" + fname
count = 0
totalSpam = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    parsePos = line.find(' ')
    spamValue = float(line[parsePos:].lstrip())
    totalSpam = totalSpam + spamValue

averageSpam = totalSpam / count
print 'Average spam confidence:',averageSpam