for t in range(int(input())):
    n = int(input())
    arr = [0]
    i = 1
    while i < n:
        x = arr[-1]
        lth = len(arr)
        new = arr[:-1]
        if x not in new:
            arr.append(0)
        else:
            kth = len(new)-new[::-1].index(x)-1
            arr.append(lth - 1 - kth)
        i += 1
    print(arr)
    print(arr.count(arr[n-1]))
