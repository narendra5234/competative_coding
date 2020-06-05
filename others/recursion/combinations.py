def get_combinations(arr, output, start, end, index, r):
    if index == r:
        print(output)
        return
    i = start
    while i <= end and i <= len(arr) + index - r:
        output[index] = arr[i]
        get_combinations(arr, output, i + 1, end, index + 1, r)
        i += 1


def input_function():
    arr = list(map(int, input().split()))
    r = int(input())
    output = [0] * r
    index = 0
    start = 0
    end = len(arr) - 1
    get_combinations(arr, output, start, end, index, r)


input_function()
