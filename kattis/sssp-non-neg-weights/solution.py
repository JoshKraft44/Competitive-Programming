import sys
import heapq


while True:
    num_nodes, num_edges, queries, start = map(int, sys.stdin.readline().split())

    if num_nodes == 0 and num_edges == 0 and queries == 0 and start == 0:
        break

    graph = [[] for _ in range(num_nodes)]

    for i in range(num_edges):
        edge1, edge2, weight = map(int, sys.stdin.readline().split())
        graph[edge1].append((edge2, weight))

    INF = float('inf')
    dist = [INF] * num_nodes
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

    for i in range(queries):
        target = int(sys.stdin.readline())

        if dist[target] == INF:
            print("impossible")
        else:
            print(dist[target])

    print()