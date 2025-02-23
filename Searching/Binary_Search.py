def rc_binary_search(items: list, item):
    mid = len(items) // 2
    if item == items[mid]:
        return True
    elif item < items[mid]:
        return rc_binary_search(items[: mid], item)
    else:
        return rc_binary_search(items[mid:], item)

def binary_search(items: list, item):
    first = 0
    last = len(items) + 1
    while first < last:
        mid = (last - first) // 2
        if item == items[mid]:
            return True
        else:
            if item < items[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

# time complexity is o(log n)
# it only works if the data is sorted
