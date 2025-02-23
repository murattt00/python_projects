def Sequential_search(items: list, item):
    for i in items:
        if i == item:
            return True
        if i > item:  # if item is missing (not in the list)
            return False
    return False
# best case o(1)
# worst case o(n)
# average case o(n/2)

print(Sequential_search([1, 2, 3, 4, 5], 2))
