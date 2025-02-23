hash_table = [None] * 11


def h(item):
    return item % 11


def put(item):
    if hash_table[h(item)]:
        hash_table[h(item) + 1] = item
    else:
        hash_table[h(item)] = item

def contains(item):
    return hash_table[h(item)] == item


put(54)
put(26)
put(93)
put(17)
put(77)
put(31)
put(22)

print(hash_table)  # time complexity is always o(1) (fastest searching method)
