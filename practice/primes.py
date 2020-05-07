from math import sqrt

for t in range(int(input())):
    first, last = map(int, input().split())
    for num in range(first, last + 1):
        c=0
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    c+=1
            if c!=0:
                print(num)