import sys

input = sys.stdin.readline


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a == root_b:
        return False

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return True


while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    edges = []

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    mst_cost = 0
    mst_edges = []

    for w, u, v in edges:
        if union(u, v, parent, rank):
            mst_cost += w

            if u > v:
                u, v = v, u

            mst_edges.append((u, v))

            if len(mst_edges) == n - 1:
                break

    if len(mst_edges) != n - 1:
        print("Impossible")
    else: 
        mst_edges.sort()
        print(mst_cost)
        for u, v in mst_edges:
            print(u, v)