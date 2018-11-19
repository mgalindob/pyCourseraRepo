largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done': break

    try:
        inNumber = int(num)
        if largest is None and smallest is None:
            largest = inNumber
            smallest = inNumber
        else:
            if inNumber > largest:
                largest = inNumber
            if inNumber < smallest:
                smallest = inNumber

    except:
        print ('Invalid input')
        continue

print ('Maximum is', largest)
print ('Minimum is', smallest)