input = int(input())
count = 0

for i in range(1, input):
        for j in range (((int(i ** (1 / 3)) - 3)), ((int(i ** (1/3)) + 3)), 3):
            if ((j * (j+1) * (j+2)) == i):
                count += 1


print(count)
