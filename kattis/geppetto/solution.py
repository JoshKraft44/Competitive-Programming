# Geppetto
# https://open.kattis.com/problems/geppetto

ingredients, num_pairs = map(int, input().split())

prohibited = set()
try: 
    for i in range(num_pairs):
        ing_1, ing_2 = map(int, input().split()) 
        prohibited.add((min(ing_1, ing_2), max(ing_1, ing_2)))

except EOFError: 
    print(2 ** ingredients)
    exit()




valid_pizzas = 0
possible = 2 ** ingredients

all_masks = []

for mask in range(possible): 
    isValid = True 

    for ing_1, ing_2 in prohibited:

        if (mask & (1 << (ing_1 - 1))) and (mask & (1 << (ing_2 - 1))): 
            isValid = False
            break 

    if isValid: 
        valid_pizzas += 1

print(valid_pizzas)





