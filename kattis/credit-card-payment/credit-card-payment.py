# Credit Card Payment
# https://open.kattis.com/problems/creditcardpayment

from decimal import Decimal, ROUND_HALF_UP
numberOfCases = int(input())

def toCents(s: str) -> int:
    return int((Decimal(s) * 100).to_integral_value(rounding = ROUND_HALF_UP))

for i in range(numberOfCases):
    count = 0
    done = False

    rate, balance, paid = input().split()

    rate_2 = int((Decimal(rate) * 100).to_integral_value(rounding = ROUND_HALF_UP))
    balance = toCents(balance)
    paid = toCents(paid)
    for j in range(1200): 
        interest = (balance * rate_2 + 5000) // 10000
        balance = balance + interest - paid

        count += 1
        if balance <=0: 
            print(count)
            done = True
            break
    if (done == False): 
        print("impossible")