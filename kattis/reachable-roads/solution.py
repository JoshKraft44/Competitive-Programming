from collections import defaultdict
import sys 


def DFS(node, graph, visited): 
    visited[node] = True
    connected = graph[node]
    for neighbor in connected: 
        if visited[neighbor]: 
            continue
        else: 
            DFS(neighbor, graph, visited)

        

numCases = int(sys.stdin.readline())
for i in range(numCases): 
    graph = defaultdict(list)
    cities = int(sys.stdin.readline())
    endpoints = int(sys.stdin.readline())
    for i in range(endpoints): 
        end_a, end_b = map(int, sys.stdin.readline().split())
        graph[end_a].append(end_b)
        graph[end_b].append(end_a)

    visited = [False] * cities 
    components = 0
    for node in range(cities): 
        if visited[node]: 
            continue
        else: 
            DFS(node, graph, visited)
            components += 1

    print(components-1)


# Figuring out how to determine a connection between all cities took me longer than it should have. 
# The number of required DFS / BFS is the number of roads that need to be added.
# I made some small mistakes: 
# "if node in visited" (always true) vs "if visited[node]" (lol)
# not passing graph / visited list parameters (first attempt) & assuming i needed to return them later 
# biggest insight: lists are mutable *and* passed by reference, so changes to the visited list are propagated. 
# changes to an integer value, if necessary, would not be, and i would have to return the int from the function. 


