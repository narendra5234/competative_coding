def num(arr, n, k):
    s = ''.join(map(str, arr))
    return s.count(str(k))
