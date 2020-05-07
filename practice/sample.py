for t in range(int(input())):
    m, n = map(int, input().split())
    l = [int(input()) for i in range(m)]
    l.sort(reverse=True)
    a = n
    sum = 0
    for i in l:
        if i <= a:
            sum += i
            a = a - i
    if sum == n:
        print("Yes")
    else:
        print("No")
