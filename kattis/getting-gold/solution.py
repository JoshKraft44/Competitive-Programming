import sys 
sys.setrecursionlimit(10 ** 6)

width, height = map(int, sys.stdin.readline().split())


grid = []
gold = []
count = 0

def DFS(node, graph, visited, gold): 
    x = int(node[0])
    y = int(node[1])
    if graph[x][y] == 'G': 
        gold[x][y] = 1
    visited[x][y] = True
    if (graph[x][y+1] == 'T') or (graph[x+1][y] == 'T') or (graph[x][y-1] == 'T') or (graph[x-1][y] == 'T'): 
        return
    
    if not visited[x][y+1]: 
        if graph[x][y+1] != '#': 
            DFS((x, y+1), grid, visited, gold)
    if not visited[x-1][y]: 
        if graph[x-1][y] != '#': 
            DFS((x-1, y), grid, visited, gold)
    if not visited[x][y-1]: 
        if graph[x][y-1] != '#': 
            DFS((x, y-1), grid, visited, gold)
    if not visited[x+1][y]: 
        if graph[x+1][y] != '#': 
            DFS((x+1, y), grid, visited, gold)
    return


for _ in range(height): 
    row = list(sys.stdin.readline().strip())
    grid.append(row)




for x in range(height): 
    for y in range(width): 
        if grid[x][y] == 'P': 
            start = (x, y)


visited = [[False] * (width) for _ in range(height)]
gold = [[0] * (width) for _ in range(height)]
DFS(start, grid, visited, gold)

for i in gold: 
    for j in i: 
        if j == 1: 
            count += 1
print(count)


# This question felt quite straightforward after doing reachable roads. It took me a minute to figure out 
# what i thought would be the best way to store the data of the graph. However, making a list of lists 
# and indexing worked perfectly. 