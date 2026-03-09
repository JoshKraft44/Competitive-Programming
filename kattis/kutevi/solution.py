# Kutevi
# https://open.kattis.com/problems/kutevi

import math

numberKnown, numberUnknown = input().split()
numberKnown = int(numberKnown)
numberUnknown = int(numberUnknown)

knownAngles = list(map(int, input().split()))
unknownAngles = list(map(int, input().split()))

currentGCD = 360

for angle in knownAngles:
    currentGCD = math.gcd(currentGCD, angle)

for angle in unknownAngles:
    if angle % currentGCD == 0:
        print("YES")
    else:
        print("NO")