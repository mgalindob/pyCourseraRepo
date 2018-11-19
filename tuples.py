fname = input("Enter file:")
fname = "Data/" + fname

try:
    handle = open(fname)
except:
    print ('File cannot be opened:', fname)
    exit()

senders = dict()
value = None

for line in handle:
    if not line.startswith("From "): continue
    address = line.split()
    address = address[5].split(':')
    address = address[0]

    if address not in senders:
        senders[address] = 1
    else:
        senders[address] += 1

lst = senders.keys()
lst.sort()

for key in lst:
    print (key, senders[key])