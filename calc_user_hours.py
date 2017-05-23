#inhrs = raw_input("Enter Hours:")
#hrs = float(inhrs)
hrs = float(80)

if hrs > 40:
    calc_hrs = 40 * 10.50
    exthrs = float(hrs) - 40
    calc_exthrs = float(exthrs) * 15.75
    tot_hrs = float(calc_hrs) + float(calc_exthrs)
    print tot_hrs

else:
    tot_hrs = float(hrs) * 10.50
    print tot_hrs