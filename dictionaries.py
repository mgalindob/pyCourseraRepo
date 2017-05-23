fname = raw_input("Enter file:")
fname = "Data/" + fname

try:
    handle = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

senders = dict()
value = None

for line in handle:
    if not line.startswith("From "): continue
    address = line.split()
    address = address[1]

    if address not in senders:
        senders[address] = 1
    else:
        senders[address] += 1

for key in senders:
    if value is None:
        value = senders[key]
    else:
        if senders[key] > value:
            value = senders[key]
            pcommitter = key
            pcommitterval = value

print pcommitter, pcommitterval
