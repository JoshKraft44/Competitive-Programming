global coins
global number
number = 0
coins = [1,4,7,8]

minCoins = 100000

value = 14



def totalCoins(dollars, currency, number): 
    if (dollars == 0): 
        return number
    number += 1
    for coin in coins: 
        return min(totalCoins(dollars - coin, currency, number))


totalCoins(value, coins, 0)