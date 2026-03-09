# Shuffling Along
# https://open.kattis.com/problems/shufflingalong

from math import gcd

deck_size, shuffle_type = input().split()
deck_size = int(deck_size)

if shuffle_type == "out":
    first_half = (deck_size + 1) // 2
else:
    first_half = deck_size // 2

second_half = deck_size - first_half

new_pos = [0] * deck_size

for i in range(first_half):
    if shuffle_type == "out":
        new_pos[i] = 2 * i      
    else:
        new_pos[i] = 2 * i + 1 

for i in range(first_half, deck_size):
    if shuffle_type == "out":
        new_pos[i] = 2 * (i - first_half) + 1
    else:
        new_pos[i] = 2 * (i - first_half)      


visited = [False] * deck_size
answer = 1

for i in range(deck_size):
    if visited[i]:
        continue

    cycle_len = 0
    current = i
    while not visited[current]:
        visited[current] = True
        current = new_pos[current]
        cycle_len += 1

    answer = answer * cycle_len // gcd(answer, cycle_len)

print(answer)