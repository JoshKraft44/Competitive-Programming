import sys 

num_cases = int(sys.stdin.readline())
inf = float('inf')


def dp(distances, num_climbs, current_height, memo):
    if (num_climbs, current_height) in memo:
        return memo[(num_climbs, current_height)]
    while num_climbs > 0:
        distance = distances[len(distances) - num_climbs]
        if current_height - distance < 0:
            rest_h, rest_p = dp(distances, num_climbs - 1, current_height + distance, memo)
            result = max(current_height + distance, rest_h), 'U' + rest_p
            memo[(num_climbs, current_height)] = result
            return result

        up_h, up_p = dp(distances, num_climbs - 1, current_height + distance, memo)
        up_h = max(current_height + distance, up_h)
        down_h, down_p = dp(distances, num_climbs - 1, current_height - distance, memo)
        down_h = max(current_height - distance, down_h)
        if up_h <= down_h:
            result = up_h, 'U' + up_p
        else:
            result = down_h, 'D' + down_p
        memo[(num_climbs, current_height)] = result
        return result
    if current_height != 0:
        return inf, ''
    return 0, ''

for i in range(num_cases):
    num_climbs = int(sys.stdin.readline())
    distances = []
    distances = tuple(map(int, sys.stdin.readline().split()))
    current_height = 0
    memo = {}
    answer, path = dp(distances, num_climbs, current_height, memo)
    if answer == inf:
        print("IMPOSSIBLE")
    else:
        print(path)






