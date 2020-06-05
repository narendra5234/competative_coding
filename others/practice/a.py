arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr) - 1):
    sum += arr[i] >= arr[i + 1]
    