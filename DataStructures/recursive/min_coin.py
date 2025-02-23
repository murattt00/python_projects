def min_change(coins: list, change: int):
    min_coin = change
    if change in coins:
        return 1
    else:
        for coin in coins:
            if coin <= change:
                num_coin = 1 + min_change(coins, change - coin)
                if num_coin < min_coin:
                    min_coin = num_coin
    return min_coin

print(min_change([1, 5, 10, 25], 63))
