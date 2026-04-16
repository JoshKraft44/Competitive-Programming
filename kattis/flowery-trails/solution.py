import sys
import heapq

def dijkstra(start, graph, n):
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


points, trails = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(points)]
edges = []

for i in range(trails):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u].append((v, w))
    graph[v].append((u, w))
    edges.append((u, v, w))

dist_start = dijkstra(0, graph, points)
dist_end = dijkstra(points - 1, graph, points)

shortest_path_length = dist_start[points - 1]

total = 0

for u, v, w in edges:
    if dist_start[u] + w + dist_end[v] == shortest_path_length or dist_start[v] + w + dist_end[u] == shortest_path_length:
        total += w

print(total * 2)   