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

num_bridges = int(sys.stdin.readline())

uf = UnionFind(2 * num_bridges)

names = defaultdict(int)
count = 0

for i in range(num_bridges):
    a, b = input().split()

    if a not in names:
        names[a] = count
        count += 1
    if b not in names:
        names[b] = count
        count += 1

    uf.union(names[a], names[b])
    print(uf.size(names[a]))