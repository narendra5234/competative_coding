# while (True):
#     n = int(input())
#     if (n == 0):
#         break
#     a = [int(i) for i in input().split()]
#     b = [0] * n
#     for i in range(n):
#         b[a[i] - 1] = i + 1
#     if (a == b):
#         print("ambiguous")
#     else:
#         print("not ambiguous")
# import pdb
n = int(input())
arr = [int(e) for e in input().split()]
zer = [-1]
for i in range(n):
    if arr[i] == 0:
        zer.append(i)#-1146i
zer.append(n)
diff = []
for i in range(1,len(zer)):
    diff.append(zer[i]-zer[i-1])
# pdb.set_trace()
print(max(diff)-1)