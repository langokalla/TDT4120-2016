from sys import stdin

Inf = 1000000000


def min_coins_greedy_list(coins, value):
    # SKRIV DIN KODE HER
    if value == 0:
        return []
    for c in coins:
        if c <= value:
            return [c] + min_coins_greedy_list(coins, value-c)


def min_coins_greedy(coins, value):
    return len(min_coins_greedy_list(coins, value))

"""
def min_coins_dynamic(coins, value):
    global memoized                                             # Instansier den globale memoiseringen
    min_coins = value                                           # Minste antall coins brukt
    if value in coins:
        memoized[value - 1] = 1
        return 1
    elif memoized[value - 1] > 0:
        return memoized[value - 1]
    else:
        for i in [c for c in coins if c <= value]:              # Går gjennom alle coins mindre enn verdien
            num_coins = 1 + min_coins_dynamic(coins, value - i) # 1 for å ha brukt en coin, + for å se etter resten.
            if num_coins < min_coins:                           # Hvis antall coins brukt er mindre enn min coin brukt
                min_coins = num_coins
                memoized[value - 1] = min_coins                 # Husker verdien
    return min_coins

"""


def min_coins_dynamic(coins, value):
    results = [Inf] * (value + 1)
    usefulCoins = []
    for c in coins:
        if c <= value:
            results[c] = 1
            usefulCoins.append(c)
    for curVal in range(1, value + 1):
        if results[curVal] != Inf:
            continue
        best = Inf
        for c in usefulCoins:
            if c <= curVal:
                current = 1 + results[curVal - c]
                if current < best:
                    best = current
        results[curVal] = best
    return results[value]


def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    return False

"""
coins = [1]
coins.sort()
coins.reverse()
value = 1024
memoized = [0]*value
print(min_coins_dynamic(coins, value))
"""

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        value = int(line)
        memoized = [0] * value
        print(min_coins_greedy(coins, value))
else:
    for line in stdin:
        value = int(line)
        memoized = [0] * value
        print(min_coins_dynamic(coins, value))
