from sys import stdin


def min_coins_greedy(coins, value):
    i = 0
    ant_mynt = 0
    while value > 0:
        while coins[i] > value:
            i += 1
        mul = value // coins[i]
        value = value - (coins[i] * mul)
        ant_mynt += mul
    return ant_mynt


def min_coins_dynamic(coins, value):
    # Inneholder myntkombos. som bruker i-1 mynter, hvis den samme ikke er der med færre.

    myntkombinasjoner = [[]]

    # Filtrer ut ubrukelige mynter, stopp hvis en mynt dekker behovet.

    for coin in coins:
        if coin < value:
            myntkombinasjoner[0].append(coin)
        elif coins == value:
            return 1

    taken = {}
    while True:
        myntkombinasjoner.append([])
        for previous_sum in myntkombinasjoner[-2]:
            for coin in myntkombinasjoner[0]:
                sum = coin + previous_sum
                if sum > value:
                    continue
                if sum == value:
                    return len(myntkombinasjoner)
                if sum not in taken:
                    taken[sum] = True
                    myntkombinasjoner[-1].append(sum)


def can_use_greedy(coins):
    return False


coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))