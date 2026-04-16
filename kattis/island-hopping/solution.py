import math, sys


def prim(points): 
    n = len(points)

    in_mst = [False] * n
    best = [float('inf')] * n
    best[0] = 0.0
    total_cost = 0.0

    for i in range(n): 
        next_island = -1
        smallest_cost = float('inf')

        for j in range(n): 
            if not in_mst[j] and best[j] < smallest_cost: 
                smallest_cost = best[j]
                next_island = j
        
        in_mst[next_island] = True
        total_cost += best[next_island]

        x1, y1 = points[next_island]

        for j in range(n): 
            if not in_mst[j]: 
                x2, y2 = points[j]
                distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

                if distance < best[j]: 
                    best[j] = distance

    return total_cost


num_cases = int(sys.stdin.readline())     
for i in range(num_cases): 
    points = []
    num_islands = int(sys.stdin.readline())     
    for i in range(num_islands): 
        x, y = sys.stdin.readline().split()
        x = float(x)
        y = float(y)
        points.append((x, y))

    print(prim(points))


# Basically a complete graph, so don't compute all N^2 possible edges and sort or it will be too slow
# (1 million TLE's working with Ethan)