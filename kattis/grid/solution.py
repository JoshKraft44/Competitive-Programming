import sys
from collections import deque

rows, cols = map(int, sys.stdin.readline().split())

grid = []
for i in range(rows):
    grid.append(sys.stdin.readline().strip())

dist = [[-1] * cols for _ in range(rows)]
dist[0][0] = 0

queue = deque()
queue.append((0, 0))

while queue:
    r, c = queue.popleft()

    jump = int(grid[r][c])

    directions = [(jump, 0), (-jump, 0), (0, jump), (0, -jump)]

    for dr, dc in directions:
        new_r = r + dr
        new_c = c + dc

        if 0 <= new_r < rows and 0 <= new_c < cols:
            if dist[new_r][new_c] == -1:
                dist[new_r][new_c] = dist[r][c] + 1
                queue.append((new_r, new_c))

print(dist[rows - 1][cols - 1])

# Thoughts: 
# Each cell defines its own edges but all edges have equal cost,
# so BFS returns the minimum number of moves.
