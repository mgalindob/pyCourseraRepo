fname = raw_input("Enter file name: ")
fname = "Data/" + fname
count = 0
fh = open(fname)

for line in fh:
    line = line.rstrip()
    line = line.split()
    emptyVal = len(line)
    if emptyVal > 0:
        if line[0]=="From":
            print line[1]
            count=count+1


print "There were", count, "lines in the file with From as the first word"