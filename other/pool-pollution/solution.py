import sys
from collections import defaultdict

class UnionFind:
    def __init__(self, size: int) -> None:
        self.p = [i for i in range(size)]
        self.r = [0 for _ in range(size)]
        self.s = [1 for _ in range(size)]

    def find(self, n: int) -> int:
        stack = []
        i = n
        while self.p[i] != i:
            stack.append(i)
            i = self.p[i]
        for j in stack:
            self.p[j] = i
        return i

    def union(self, a: int, b: int) -> None:
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        if self.r[pa] < self.r[pb]:
            self.p[pb] = pa
            self.s[pa] += self.s[pb]
        elif self.r[pb] < self.r[pa]:
            self.p[pa] = pb
            self.s[pb] += self.s[pa]
        else:
            self.p[pb] = pa
            self.s[pa] += self.s[pb]
            self.r[pa] += 1

    def size(self, n: int) -> int:
        return self.s[self.find(n)]

num_pools, num_pipes, num_contaminated = map(int, sys.stdin.readline().split())
capacities = list(map(int, sys.stdin.readline().split()))
uf = UnionFind(num_pools)
for i in range(num_pipes): 
    a, b = map(int, sys.stdin.readline().split())
    uf.union(a - 1, b - 1)

total = []

contaminated_pools = list(map(int, sys.stdin.readline().split()))
for pool in contaminated_pools: 
    total.append(uf.find(pool - 1))

output = 0
for i in range(num_pools):
    if uf.find(i) not in total: 
        output += capacities[i]

print(output)




