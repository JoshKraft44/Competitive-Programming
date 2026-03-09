# Paintings
# https://open.kattis.com/problems/paintings

import sys

num_cases = int(sys.stdin.readline())
for _ in range(num_cases):
    n = int(sys.stdin.readline().strip())
    colors = sys.stdin.readline().strip().split()
    num_pairs = int(sys.stdin.readline().strip())
    prohibited = set()
    for _ in range(num_pairs):
        a, b = sys.stdin.readline().strip().split()
        prohibited.add((a, b))
        prohibited.add((b, a))

    def count_valid(last, used):
        if len(used) == n:
            return 1
        total = 0
        for i, color in enumerate(colors):
            if i in used:
                continue
            if last and (last, color) in prohibited:
                continue
            used.add(i)
            total += count_valid(color, used)
            used.remove(i)
        return total

    def can_complete(last, used):
        if len(used) == n:
            return True
        for index, color in enumerate(colors):
            if index in used:
                continue
            if last and (last, color) in prohibited:
                continue
            used.add(index)
            if can_complete(color, used):
                used.remove(index)
                return True
            used.remove(index)
        return False


    result = []
    used = set()
    for _ in range(n):
        for i, color in enumerate(colors): 
            if i in used:
                continue
            last = result[-1] if result else None
            if last and (last, color) in prohibited:
                continue
            used.add(i)
            if can_complete(color, used):
                result.append(color)
                break
            used.remove(i)

    print(count_valid(None, set()))
    print(' '.join(result))