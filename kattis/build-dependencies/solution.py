from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def DFS(filename, dict, visited, seen): 
    seen.add(filename)
    for i in dict[filename]:
            if i not in seen: 
                DFS(i, dict, visited, seen)
    visited.append(filename)
                

numFiles = int(sys.stdin.readline())

dict = defaultdict(set)

for _ in range(numFiles): 
    input1 = sys.stdin.readline()
    input2 = input1.split(":")
    name = input2[0].strip()
    deps = input2[1].split()
    for i in deps: 
        dict[i].add(name)

startFile = sys.stdin.readline().strip()

visited = []

DFS(startFile, dict, visited, set())

dependencies = '\n'.join(reversed(visited))
print(dependencies)


# My key insight from solving this problem was that I needed to have a set for seen nodes to
# ensure I only visited each node once, *and* a visited list to be able to keep track of visited 
# nodes, since using just the set would ruin my order, and list iteration for traversal would 
# be too slow. 