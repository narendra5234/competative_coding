def solve(a, c, b, M, N, X):
    diff = []
    for i in range(M+1):
        diff.append(b[i] - a[i])
    c.sort()
    diff.sort()
    new = diff+c
    new.sort()
    sum=0
    i=0
    count=0
    while sum<X:
        sum+=new[i]
        count+=1
        i+=1
    return count-1



N, M, X = map(int, input().split(" "))
a = []
b = []
for i in range(N):
    x, y = map(int, input().split(" "))
    a.append(x)
    b.append(y)
c = list(map(int, input().split(" ")))

out_ = solve(a, c, b, M, N, X)
print(out_)