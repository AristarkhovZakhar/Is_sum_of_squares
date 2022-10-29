def binsearch(b, x):
    i, j = 0, len(b) - 1
    while i+1 != j:
        k = (i + j)//2
        if b[k] < x:
            i = k
        else:
            j = k
    return j
