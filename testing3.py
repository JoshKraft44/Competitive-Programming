import sys
numberOfCases = int(input())

for i in range(numberOfCases):
    leftover = 0
    rate, balance, paid = input().split()
    rate = float(rate)
    balance = float(balance)
    paid = float(paid)
    for j in range(50): 
        percent = rate / 100
        leftover = (((balance * percent) + balance) - paid) 
        balance = leftover
        print(balance)
        j += 1
        if balance <=0: 
            print(j)
            break
        print("impossible")