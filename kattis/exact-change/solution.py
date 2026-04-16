import sys

num_cases = int(sys.stdin.readline())
inf = float('inf')


def dp(coins, n, cost, idx, amount, memo):
    if amount >= cost:
        return amount, 0
    if idx == n:
        return inf, inf
    if (idx, amount) in memo:
        return memo[(idx, amount)]

    t1, c1 = dp(coins, n, cost, idx + 1, amount + coins[idx], memo)
    c1 += 1

    t2, c2 = dp(coins, n, cost, idx + 1, amount, memo)

    if t1 < t2 or (t1 == t2 and c1 < c2):
        result = t1, c1
    else:
        result = t2, c2

    memo[(idx, amount)] = result
    return result


for i in range(num_cases):
    cost = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    coins = []
    for j in range(n):
        coins.append(int(sys.stdin.readline()))
    memo = {}
    total, num = dp(coins, n, cost, 0, 0, memo)
    print(total, num)
