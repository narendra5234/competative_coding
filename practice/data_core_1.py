
from collections import deque

arr = [12, 1, 78, 90, 57, 89, 56]
k = 3
n=len(arr)
queue = deque()
l=[]
for i in range(k):
    while queue and arr[i] >= arr[queue[-1]]:
        queue.pop()
    queue.append(i)
for i in range(k, n):
    l.append(arr[queue[0]])
    while queue and queue[0] <= i - k:
        queue.popleft()

    while queue and arr[i] >= arr[queue[-1]]:
        queue.pop()
    queue.append(i)
l.append(arr[queue[0]])
