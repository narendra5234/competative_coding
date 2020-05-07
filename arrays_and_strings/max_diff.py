class MaxDifference:
    # brute force----O(n2)
    @staticmethod
    def max_difference(arr):
        max_diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                max_diff = max(max_diff, arr[j] - arr[i])
        print(max_diff)

    # Optimized -----O(n)
    @staticmethod
    def max_difference_1(arr):
        max_diff = arr[1] - arr[0]
        i_value = arr[0]
        for j in range(1, len(arr)):
            max_diff = max(max_diff, arr[j] - i_value)
            i_value = min(i_value, arr[j])  # we get max diff when i_value is min
        print(max_diff)


obj = MaxDifference()
obj.max_difference_1([30, 10, 8, 2])
