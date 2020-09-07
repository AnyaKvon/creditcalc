import math
import argparse


def months(credit_principal, payment, interest):
    p_credit = credit_principal
    p = payment
    i = (interest * 0.01) / 12
    x = p / (p - i * p_credit)
    n = math.ceil(math.log(x, 1 + i))
    if n % 12 == 0:
        print(f'It will take {n // 12} years to repay this credit!')
    elif n // 12 > 0 and n % 12 > 0:
        print(f'It will take {n // 12} years and {math.ceil(n % 12)} months to repay this credit!')
    else:
        print(f'It will take {math.ceil(n // 12)} months to repay this credit!')

    if n * payment - p_credit > 0:
        print(f'Overpayment = {round(n * payment - p_credit)}')


def annuity(credit_principal, periods, interest):
    p_credit = credit_principal
    n = periods
    i = (interest / 100) / 12
    x = math.ceil(p_credit * i * pow(1 + i, n) / (pow(1 + i, n) - 1))
    print(f'Your annuity payment = {x}!')
    if x * n - p_credit > 0:
        print(f'Overpayment = {x * n - p_credit}')


def credit(payment, periods, interest):
    payment = payment
    n = periods
    i = (interest / 100) / 12
    P = math.floor(payment / (i * pow(1 + i, n) / (pow(1 + i, n) - 1)))
    print(f'Your credit principal = {P}!')
    if n * payment - P > 0:
        print(f'Overpayment = {round(n * payment - P)}')


def diff(principal, periods, interest):
    p_credit = principal
    n = periods
    i = (interest * 0.01) / 12
    common = 0
    for j in range(n):
        m = math.ceil(p_credit / n + i * (p_credit - (p_credit * j) / n))
        common += m
        print(f'Month {j + 1}: payment is {m}')
    if common - p_credit > 0:
        print(f'\nOverpayment = {common - p_credit}')


parser = argparse.ArgumentParser()
parser.add_argument('--type', help='the type of payment')
parser.add_argument('--principal', type=int, help='principal credit')
parser.add_argument('--periods', type=int, help=' parameter denotes the number of months and/or years needed to repay the credit')
parser.add_argument('--interest', type=float, help='nominal interest rate')
parser.add_argument('--payment', type=float, help='which refers to the monthly payment')
parser.parse_args()
args = parser.parse_args()
if args.type == 'annuity':
    if args.principal and args.interest and args.periods:
        annuity(args.principal, args.periods, args.interest)
    elif args.payment and args.interest and args.periods:
        credit(args.payment, args.periods, args.interest)
    elif args.principal and args.interest and args.payment:
        months(args.principal, args.payment, args.interest)
    else:
        print('Incorrect parameters.')
elif args.type == 'diff':
    if args.principal > 0 and args.interest > 0 and args.periods > 0:
        diff(args.principal, args.periods, args.interest)
    else:
        print('Incorrect parameters.')
else:
    print('Incorrect parameters')
