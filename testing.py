base = int(input())
for i in range(base, 1000000000): 
    digits = [int(digit) for digit in str(base)]
    total = 0
    for i in digits: 
        total += i
    if (base % total == 0): 
        break
    else: 
        base += 1
print(base)

    
