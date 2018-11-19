fname = input('Enter file name: ')
fname = "Data/" + fname
fh = open(fname)

for line in fh:
    line = line.rstrip().upper()
    print (line)