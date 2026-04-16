import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break

    capacity, n = map(int, line.split())

    values = []
    weights = []

    for i in range(n):
        v, w = map(int, sys.stdin.readline().split())
        values.append(v)
        weights.append(w)

    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]

            if w >= weights[i - 1]:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    w = capacity
    chosen = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= weights[i - 1]

    print(len(chosen))
    print(" ".join(map(str, chosen)))

# Older solution: too slow 
# Memoization 
