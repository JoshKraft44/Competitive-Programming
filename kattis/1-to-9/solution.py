# 1 to 9
# From Lecture ??

# Given number N, return all numbers x such that X / N = Y and set (X, Y) E {0,1,2,3,4,5,6,7,8,9}


N = int(input())
for x in range(1234, 98766, 1): 
    boolean = True
    if ( x% N != 0): 
        continue
    y = x // N
    numbers = list(str(x)) + list(str(y))
    numbers = list(map(int, numbers))

    if len(numbers) < 10: 
        numbers.append(0)
    if set(numbers) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
        print(x, y)
    
    