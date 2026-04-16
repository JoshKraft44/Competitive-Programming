import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return

    parent[root_b] = root_a



n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n)]
rank = [0] * n

for i in range(m):
    parts = sys.stdin.readline().split()

    if parts[0] == "=":
        a = int(parts[1])
        b = int(parts[2])
        union(a, b)

    else: 
        a = int(parts[1])
        b = int(parts[2])

        if find(a) == find(b):
            print("yes")
        else:
            print("no")