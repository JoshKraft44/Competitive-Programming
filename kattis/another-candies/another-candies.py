# Another Candies
# https://open.kattis.com/problems/anothercandies

numberCases = int(input())
def solve(): 
    global totalCandies
    totalCandies = 0
    for _ in range(numberCases): 
        try: 
            numberChildren = input()
            if (numberChildren == ''): 
                solve()   
            else: numberChildren = int(numberChildren)             
            for _ in range(numberChildren): 
                candies = int(input())
                totalCandies += candies
            if (totalCandies % numberChildren) == 0: 
                print("YES")
            else: print("NO")
        except EOFError: 
            exit()

solve()
