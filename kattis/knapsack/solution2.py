import sys

data = sys.stdin.read().split()
index = 0
output = []

while index < len(data):
    capacity = int(data[index])
    index += 1
    n = int(data[index])
    index += 1

    values = [0] * n
    weights = [0] * n

    for i in range(n):
        values[i] = int(data[index])
        index += 1
        weights[i] = int(data[index])
        index += 1

    dp = [0] * (capacity + 1)

    path_id = [-1] * (capacity + 1)

    path_item = []
    path_prev = []

    for i in range(n):
        value = values[i]
        weight = weights[i]

        for w in range(capacity, weight - 1, -1):
            new_val = dp[w - weight] + value

            if new_val > dp[w]:
                dp[w] = new_val

                new_node = len(path_item)
                path_item.append(i)
                path_prev.append(path_id[w - weight])

                path_id[w] = new_node

    best_w = 0
    for w in range(1, capacity + 1):
        if dp[w] > dp[best_w]:
            best_w = w

    chosen = []
    current = path_id[best_w]

    while current != -1:
        chosen.append(path_item[current])
        current = path_prev[current]

    output.append(len(chosen))
    output.append(" ".join(map(str, chosen)))

for i in output: 
    print(i) 