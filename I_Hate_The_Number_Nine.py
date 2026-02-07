MOD = 1000000007

t = int(input())
for _ in range(t):
    d = int(input())
    a = pow(9, d, MOD)
    b = pow(9, d - 1, MOD)
    print((a - b) % MOD)