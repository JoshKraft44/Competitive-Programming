# Counting Coins
# https://open.kattis.com/problems/countingcoins

coins = [1, 4, 7, 8]
value = 14

def totalCoins(dollars, coins, number):
    if dollars == 0:
        return 0
    if dollars < 0:
        return 10**18 
    if dollars in number:
        return number[dollars]

    best = 10**18
    for coin in coins:
        attempt = 1 + totalCoins(dollars - coin, coins, number)
        if attempt < best:
            best = attempt

    number[dollars] = best
    return best

ans = totalCoins(value, coins, {})
print(ans)