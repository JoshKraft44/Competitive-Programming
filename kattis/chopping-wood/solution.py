import sys
import heapq

num = int(sys.stdin.readline())
n = num + 1

v = []
freq = [0] * (n + 1)

for i in range(num):
    x = int(sys.stdin.readline())
    v.append(x)
    freq[x] += 1

if v[-1] != n:
    print("Error")
    exit()

heap = []

for i in range(1, n + 1):
    if freq[i] == 0:
        heapq.heappush(heap, i)

u = []

for i in range(num):

    if len(heap) == 0:
        print("Error")
        exit()

    leaf = heapq.heappop(heap)
    u.append(leaf)

    parent = v[i]
    freq[parent] -= 1

    if freq[parent] == 0:
        heapq.heappush(heap, parent)

for x in u:
    print(x)