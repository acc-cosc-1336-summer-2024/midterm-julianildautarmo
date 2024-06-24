#write functions here, don't add input('') statements here!

#Part 3.1

def get_bonus_pay(sales):
    if(int(sales) < 0 or int(sales) > 1999):
        valid = False

        #direction wasnt given on what to do during the intervals between 499 and 500, 999 and 1000, 1499 and 1500
    else:
        valid = True
        if(0 <= int(sales) <=499):
            percent = 0.05
        if(500 <= int(sales) <= 999):
            percent = 0.06
        if(1000 <= int(sales) <= 1499):
            percent = 0.07
        if(1500 <= int(sales) <= 1999):
            percent = 0.08

    if(valid == False):
        bonus_p = "Invalid Argument"

    else:
        bonus_p = float(percent) * float(sales)

    return bonus_p
