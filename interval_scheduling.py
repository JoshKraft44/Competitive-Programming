numberOfIntervals = int(input())
full_array = []
count = 0 

for i in range(numberOfIntervals): 
    (x, y) = input().split()
    x = int(x)
    y = int(y)
    full_array.append((x, y))





smallest = 100
while (len(full_array) > 0): 
    values = []
    for i in range(len(full_array)):
        next = full_array[i][1]
        values.append(next)
        print(values)
        smallest = min(values)
    
    print(smallest)
    
    for item in range(len(full_array)):
        value = full_array[item][1]
        if value < smallest: 
            full_array[item].pop()

    print(full_array)
    count += 1



        

        
    
