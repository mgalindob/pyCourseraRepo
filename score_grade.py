# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

ingrade = input("Enter the grade:")

try:
    grade = float(ingrade)

    if grade < 1.1:
        if grade >= 0.9:
            print('A')
        elif grade >= 0.8:
            print('B')
        elif grade >= 0.7:
            print('C')
        elif grade >= 0.6:
            print('D')
        elif grade < 0.6:
            print('F')
    else:
        print ("Please enter a correct score")

except:
    print ("Please enter a correct score")