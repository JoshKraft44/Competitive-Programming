# Opening Ceremony
# https://open.kattis.com/problems/openingceremony

blocks = int(input())
towers = sorted(map(int, input().split()))

charges = blocks 

for i in range(1, blocks + 1):
    charges = min(charges, (blocks - i) + towers[i - 1])

print(charges)