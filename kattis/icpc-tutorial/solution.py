# ICPC Tutorial
# https://open.kattis.com/problems/icpctutorial

import math

t, n, complexity = map(int, input().split())

if complexity == 1:  # O(n!)
    log_factorial = sum(math.log(i) for i in range(1, n + 1)) if n > 0 else 0
    if log_factorial <= math.log(t):
        print("AC")
    else:
        print("TLE")
elif complexity == 2:  # O(2^n)
    if n * math.log(2) <= math.log(t):
        print("AC")
    else:
        print("TLE")
elif complexity == 3:  # O(n^4)
    if n ** 4 <= t:
        print("AC")
    else:
        print("TLE")
elif complexity == 4:  # O(n^3)
    if n ** 3 <= t:
        print("AC")
    else:
        print("TLE")
elif complexity == 5:  # O(n^2)
    if n ** 2 <= t:
        print("AC")
    else:
        print("TLE")
elif complexity == 6:  # O(n log n)
    if n == 0 or n * math.log2(n) <= t:
        print("AC")
    else:
        print("TLE")
elif complexity == 7:  # O(n)
    if n <= t:
        print("AC")
    else:
        print("TLE")