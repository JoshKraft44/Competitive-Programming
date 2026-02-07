from fractions import Fraction

n = int(input())
values = list(map(int, input().split()))

def createFraction(i: int) -> Fraction: 
    if i == n-1:
        return Fraction(1, values[i])
    else: 
        return Fraction(1, values[i] + createFraction(i + 1))


final = values[0] + createFraction(1)
print(final)
