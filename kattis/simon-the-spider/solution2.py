import sys

input = sys.stdin.readline


def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b, parent, rank):
    ra, rb = find(a, parent), find(b, parent)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True


out = []

while True:
    line = input().split()
    if not line:
        break

    n, m = int(line[0]), int(line[1])

    edges = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((w, a - 1, b - 1))

    edges.sort()

    parent = list(range(n))
    rank = [0] * n
    used = 0

    for w, a, b in edges:
        if union(a, b, parent, rank):
            used += 1

    if used != n - 1:
        out.append("disconnected")
        continue

    best = float("inf")

    for i in range(m):
        w, u, v = edges[i]

        parent2 = list(range(n))
        rank2 = [0] * n

        union(u, v, parent2, rank2)
        edges_used = 1
        added_cost = 0

        for j in range(i + 1):
            wj, a, b = edges[j]
            if union(a, b, parent2, rank2):
                added_cost += wj
                edges_used += 1
                if edges_used == n - 1:
                    break

        if edges_used == n - 1:
            best = min(best, added_cost - w)

    out.append(str(best))

for i in out: 
    print(i)