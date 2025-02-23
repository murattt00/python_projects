def insertion_sort(alist):
    for i in range(1, len(alist)):
        cur_val = alist[i]
        cur = 1
        while cur > 0 and alist[cur -1] > cur_val:
            alist[cur] = alist[cur -1]
            cur = cur - 1
        alist[cur] = cur_val
