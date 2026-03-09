# Interval Scheduling
# https://open.kattis.com/problems/intervalscheduling


# key insight - sort by end time once

numberOfIntervals = int(input())
full_array = []
count = 0

for i in range(numberOfIntervals):
    x, y = input().split()
    x = int(x)
    y = int(y)
    full_array.append((x, y))

full_array.sort(key=lambda t: t[1])

current_end = -10**18 

for i in range(len(full_array)):
    start = full_array[i][0]
    end = full_array[i][1]

    if start >= current_end:
        count += 1
        current_end = end

print(count)