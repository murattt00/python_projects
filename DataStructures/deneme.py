def min_change(coins: list, change: int):
    min_coin = change
    if change in coins:
        return 1
    else:
        for coin in coins:
            if coin < change:
                num_coin = 1 + min_change(coins, change - coin)
                if num_coin < min_coin:
                    min_coin = num_coin
    return min_coin

print(min_change([1, 5, 10, 25], 4))


def reverse(alist: list):
    if len(alist) == 1:
        return alist
    else:
        return reverse(alist[1:]) + [alist[0]]

def remove(mystack , item):
    alist = []
    for i in mystack.size():
        if mystack.peek() == item:
            mystack.pop()
            break
        else:
            alist.insert(0,mystack.pop())
    for i in alist:
        mystack.push(i)
    return mystack

