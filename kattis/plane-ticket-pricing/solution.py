import sys

S, W = map(int, sys.stdin.readline().split())

weeks = []

for _ in range(W + 1):
    data = list(map(int, sys.stdin.readline().split()))
    k = data[0]

    prices = data[1:1 + k]
    sold_estimates = data[1 + k:1 + 2 * k]

    options = []
    for i in range(k):
        options.append((prices[i], sold_estimates[i]))

    weeks.append(options)

memo = [[-1] * (S + 1) for _ in range(W + 2)]

def dp(week, seats_left):
    if week == W + 1:
        return 0

    if memo[week][seats_left] != -1:
        return memo[week][seats_left]

    best = 0

    for price, estimate in weeks[week]:
        tickets_sold = min(seats_left, estimate)
        revenue_now = price * tickets_sold
        revenue_later = dp(week + 1, seats_left - tickets_sold)

        total = revenue_now + revenue_later

        if total > best:
            best = total

    memo[week][seats_left] = best
    return best

best_revenue = dp(0, S)


best_price = None

for price, estimate in weeks[0]:
    tickets_sold = min(S, estimate)
    total = price * tickets_sold + dp(1, S - tickets_sold)

    if total == best_revenue:
        if best_price is None or price < best_price:
            best_price = price

print(best_revenue)
print(best_price)