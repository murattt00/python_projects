def selection_sort(alist):
    for i in range(len(alist)):
        min_idx = len(alist) - 1
        for j in range(i, len(alist)):
            if alist[j] < alist[min_idx]:
                min_idx = j
        if min_idx != i:
            temp = alist[i]
            alist[i] = alist[min_idx]
            alist[min_idx] = temp
