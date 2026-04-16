l = int(input())
d = int(input())
x = int(input())

listOfNum= []

for a in range(l,d+1):
    digits = [int(digit) for digit in str(a)]
    sumOfA = sum(digits)
    if x == (sumOfA):
        listOfNum.append(a)

print(min(listOfNum))
print(max(listOfNum))