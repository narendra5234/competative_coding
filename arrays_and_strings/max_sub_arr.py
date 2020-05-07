class MaxSubArray:
    # brute force
    @staticmethod
    def max_sub_array(arr):
        max_sum = arr[0]
        for i in range(len(arr) - 1):
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]
                max_sum = max(max_sum, curr_sum)
        print(max_sum)

    @staticmethod
    def max_sub_array_1(arr):
        max_sum = arr[0]
        curr_sum = arr[0]
        for j in range(1, len(arr)):
            curr_sum = max(arr[j], curr_sum + arr[j])
            max_sum = max(max_sum, curr_sum)
        print(max_sum)

obj = MaxSubArray()
obj.max_sub_array_1([1, -2, 3, -1, 2])
