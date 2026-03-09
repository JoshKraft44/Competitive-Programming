# Jumbled Communication
# https://open.kattis.com/problems/jumbledcommunication

num_bits = input()

inputs = input().split()
results = []

for i in inputs: 
    i = int(i)
    bits = []
    bits.append((i >> 0) & 1)
    for j in range(1,8):
        first_bit = (i >> j) & 1
        bits.append(first_bit ^ bits[j-1])

    result = int("".join(str(b) for b in reversed(bits)), 2)
    results.append(str(result))


print(" ".join(results))

        

