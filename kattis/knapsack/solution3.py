import sys

data = sys.stdin.buffer.read().split()
out = []
second = []
p = 0

while p < len(data):
    capacity = int(data[p])
    p += 1
    n = int(data[p])
    p += 1

    values = [0] * n
    weights = [0] * n

    for i in range(n):
        values[i] = int(data[p])
        p += 1
        weights[i] = int(data[p])
        p += 1

    dp = [0] * (capacity + 1)

    take = [bytearray(capacity + 1) for _ in range(n)]

    for i in range(n):
        value = values[i]
        weight = weights[i]

        for w in range(capacity, weight - 1, -1):
            cand = dp[w - weight] + value
            if cand > dp[w]:
                dp[w] = cand
                take[i][w] = 1

    w = capacity
    chosen = []

    for i in range(n - 1, -1, -1):
        if take[i][w]:
            chosen.append(i)
            w -= weights[i]

    chosen.reverse()

    out.append(str(len(chosen)))
    out.append(" ".join(map(str, chosen)))

sys.stdout.write("\n".join(out))