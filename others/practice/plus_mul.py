for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c1,c2=0,0
    a=l.count(2)
    b=l.count(0)
    if a>=2:
        c1=(a*(a-1))//2
    elif b>=0:
        c2=(b*(b-1))//2
    print(c1+c2)

