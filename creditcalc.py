from math import log, ceil, floor, pow
from sys import argv
ERROR_MSG = "Incorrect parameters"
a, i, p, n = None, None, None, None
if 4 <= len(argv[1:]) <= 5:
    interest = [i[11:] for i in argv if "--interest" in i]
    if len(interest) == 1:
        interest = float(interest[0])
        if interest >=0:
            i = interest / 1200
        else:
            print(ERROR_MSG)
            exit()
    else:
        print(ERROR_MSG)
        exit()
    payment = [i[10:] for i in argv if "--payment" in i]
    if len(payment) == 1:
        a = float(payment[0])
        if a < 0:
            print(ERROR_MSG)
            exit()
    principal = [i[12:] for i in argv if "--principal" in i]
    if len(principal) == 1:
        p = float(principal[0])
        if p < 0:
            print(ERROR_MSG)
            exit()
    periods = [i[10:] for i in argv if "--periods" in i]
    if len(periods) == 1:
        n = int(periods[0])
        if n < 0:
            print(ERROR_MSG)
            exit()
    if "--type=diff" in argv:
        if a is None:
            months = [ceil(p/n+(p-p*(m-1)/n)*i) for m in range(1, n+1)]
            for month, payment in enumerate(months, 1):
                print("Month {}: payment is {}".format(str(month), str(payment)))
            print("Overpayment = {}".format(int(sum(months) - p)))
        else:
            print(ERROR_MSG)
    elif "--type=annuity" in argv:
        if p is not None and a is None and n is not None:
            a = ceil((p * i * pow((1 + i), n)) / (pow(1 + i, n) - 1))
            print("Your annuity payment = {}!".format(a))
            print("Overpayment = {}".format(int(n * a - p)))
        if p is None and a is not None and n is not None:
            p = floor(a / ((i * pow((1 + i), n)) / (pow(1 + i, n) - 1)))
            print("Your loan principal = {}!".format(p))
            print("Overpayment = {}".format(int(n * a - p)))
        elif p is not None and a is not None and n is None:
            months = ceil(log((a / (a - i * p)), i + 1))
            if months == 1:
                print("It will take 1 month to repay this loan")
            elif months < 12:
                print("It will take {} months to repay this loan".format(months))
            elif months == 12:
                print("It will take 1 year to repay this loan")
            elif months == 13:
                print("It will take 1 year and 1 month to repay this loan")
            elif 13 < months < 24:
                print("It will take 1 year and {} months to repay this loan".format(months - 12))
            elif months % 12 == 0:
                print("It will take {} years to repay this loan".format(int(months / 12)))
            elif months % 13 == 0:
                print("It will take {} years and 1 month to repay this loan".format(int(months / 13)))
            else:
                years = floor(months / 12)
                months = months % 12
                print("It will take {} years and {} months to repay this loan!".format(years, months))
            print("Overpayment = {}".format(int(months * a - p)))
    else:
        print(ERROR_MSG)
        exit()
else:
    print(ERROR_MSG)
