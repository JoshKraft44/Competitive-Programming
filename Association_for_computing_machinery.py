problems, first = input().strip().split()
first = int(first)
times = list(map(int, input().strip().split()))
clock = 0
total_time = 0
solved = 0

if times[first] <= 300:
    solved += 1
    clock = times[first]
    total_time = clock

else:
    print("0 0")
    exit()

times.pop(first)

while True:
    if not times:
        print(solved, total_time)
        exit()
    next_val = min(times)
    index = times.index(next_val)
    new_clock = clock + next_val
    if new_clock <= 300:
        solved += 1
        clock = new_clock
        total_time += clock
        times.pop(index)
    else:
        print(solved, total_time)
        exit()
