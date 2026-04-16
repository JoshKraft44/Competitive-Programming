import sys
import heapq


while True:
    num_nodes, num_edges, queries, start = map(int, sys.stdin.readline().split())

    if num_nodes == 0 and num_edges == 0 and queries == 0 and start == 0:
        break

    graph = [[] for _ in range(num_nodes)]

    for i in range(num_edges):
        edge1, edge2, t0, p, d = map(int, sys.stdin.readline().split())
        graph[edge1].append((edge2, t0, p, d))

    INF = float('inf')
    dist = [INF] * num_nodes
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, t0, p, d in graph[node]:
            if current_dist <= t0:
                new_dist = t0 + d

            else:
                if p == 0:
                    continue

                wait = (p - ((current_dist - t0) % p)) % p
                new_dist = current_dist + wait + d

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    for i in range(queries):
        target = int(sys.stdin.readline())

        if dist[target] == INF:
            print("Impossible")
        else:
            print(dist[target])

    print()

# Still Dijkstra, but edges aren’t always usable immediately.Instead of dist[u] + weight, you might need to wait until 
# the next valid departure time t0 + k*p, then add travel time d. If p == 0,  edge can only be used once at t0.
