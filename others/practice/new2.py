from others.math import sqrt
for t in range(int(input())):
    n = int(input())
    for i in range(int(sqrt(n)), 0, -1):
        x = n % i
        if x == 0:
            y = n/i
            print(int(y-i))
            break
