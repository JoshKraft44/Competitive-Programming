# Interval Scheduling
# https://open.kattis.com/problems/intervalscheduling

# TLE 

numberOfIntervals = int(input())
full_array = []
count = 0

for i in range(numberOfIntervals):
    x, y = input().split()
    x = int(x)
    y = int(y)
    full_array.append((x, y))

while len(full_array) > 0:
    smallest_end = 10**18
    for i in range(len(full_array)):
        end = full_array[i][1]
        if end < smallest_end:
            smallest_end = end

    count += 1

    new_array = []
    for i in range(len(full_array)):
        start = full_array[i][0]
        if start >= smallest_end:
            new_array.append(full_array[i])

    full_array = new_array

print(count)


        

        
    
