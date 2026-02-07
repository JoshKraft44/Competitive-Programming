N = int(input())
for x in range(1234, 98766, 1): 
    if ( x% N != 0): 
        continue
    y = x // N
    numbers = list(str(x)) + list(str(y))
    numbers = list(map(int, numbers))
    if len(numbers) < 11: 
        numbers.append(0) 
    numbers.sort()
    print(numbers)
    for i in range(len(numbers)-1): 
        if (numbers[i] != (numbers[i+1] + 1)): 
            break
        print(x, y)
    