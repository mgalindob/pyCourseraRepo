def computepay(inhrs, inrt):
    hrs = float(inhrs)
    rate = float(inrt)
    xrate = ((float(rate) / 2) + float(rate))

    if hrs > 40:
        calc_hrs = 40 * rate
        exthrs = float(hrs) - 40
        calc_exthrs = float(exthrs) * xrate
        tot_hrs = float(calc_hrs) + float(calc_exthrs)
        return tot_hrs

    else:
        tot_hrs = float(hrs) * rate
        return tot_hrs


input_hrs = raw_input("Enter Hours:")
pay = computepay(input_hrs, "10.50")

print pay