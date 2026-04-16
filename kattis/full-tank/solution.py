import sys, heapq
from collections import defaultdict

def Dijkstra(start, roads, destination, capacity):
    INF = float('inf')
    dist = [[INF] * (capacity + 1) for _ in range(num_cities)]

    pq = []
    dist[start][0] = 0
    heapq.heappush(pq, (0, start, 0))

    while pq:
        cost, city, fuel = heapq.heappop(pq)

        if city == destination:
            return cost

        if cost > dist[city][fuel]:
            continue

        if fuel < capacity:
            next_cost = cost + fuel_prices[city]
            if next_cost < dist[city][fuel + 1]:
                dist[city][fuel + 1] = next_cost
                heapq.heappush(pq, (next_cost, city, fuel + 1))

        for neighbor, distance in roads[city]:
            if fuel >= distance:
                next_fuel = fuel - distance
                if cost < dist[neighbor][next_fuel]:
                    dist[neighbor][next_fuel] = cost
                    heapq.heappush(pq, (cost, neighbor, next_fuel))

    return "impossible"

num_cities, num_roads = map(int, sys.stdin.readline().split())
fuel_prices = list(map(int, sys.stdin.readline().split()))

roads = defaultdict(list)

for i in range(num_roads):
    a, b, d = map(int, sys.stdin.readline().split())
    roads[a].append((b, d))
    roads[b].append((a, d))

num_queries = int(sys.stdin.readline())


for i in range(num_queries):
    capacity, start, destination = map(int, sys.stdin.readline().split())
    print(Dijkstra(start, roads, destination, capacity))