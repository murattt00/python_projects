def buble_sorting(alist):
    for i in range(len(alist), 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp


