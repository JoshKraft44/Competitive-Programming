import sys

n = int(sys.stdin.readline())

owner = {}
sets = {}
next = 0

count = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    recipe = set(arr[1:])

    used = set()

    for x in recipe:
        if x in owner:
            used.add(owner[x])

    ok = True
    for i in used:
        if not sets[i].issubset(recipe):
            ok = False
            break

    if not ok:
        continue

    new_set = set(recipe)

    for i in used:
        for x in sets[i]:
            owner.pop(x)
        del sets[i]

    i = next
    next += 1

    sets[i] = new_set
    for x in new_set:
        owner[x] = i

    count += 1

print(count)