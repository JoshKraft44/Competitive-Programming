# Assigning Workstations
# https://open.kattis.com/problems/assigningworkstations

import heapq



researchers, lockTime = map(int, input().strip().split())
times = []

for i in range(researchers):
    arriveTime, stayTime = map(int, input().strip().split())
    times.append((arriveTime, stayTime))

times.sort()
free = []
saved = 0

for arriveTime, stayTime in times:
    
    
    while free and free[0] + lockTime < arriveTime:
        heapq.heappop(free)

    if free and free[0] <= arriveTime: 
        heapq.heappop(free)
        saved += 1

    heapq.heappush(free, arriveTime + stayTime)

print(saved)