import heapq
import sys

rows, cols = map(int, sys.stdin().readline().split())

def get_id(row, col):
    return row * cols + col

num_nodes = rows * cols
start = num_nodes
end = num_nodes + 1
total = num_nodes + 2
answer = 0

graph = [[] for _ in range()]

grid = [[map(int, sys.stdin().readline().split()) for _ in range(rows)]]

for row in rows: 
    for col in cols: 
        idx = get_id(row, col)

        if row + 1 < rows: 
            neighbour = get_id(row + 1, col)
            weight = max(grid[idx], grid[neighbour])
            graph[neighbour].append(weight, idx)
            graph[idx].append(weight, neighbour)


        if col + 1 < cols: 
            neighbour = get_id(row, col + 1)
            weight = max(grid[idx], grid[neighbour])
            graph[neighbour].append(weight, idx)
            graph[idx].append(weight, neighbour)


for row in rows: 
    idx = get_id(graph[])