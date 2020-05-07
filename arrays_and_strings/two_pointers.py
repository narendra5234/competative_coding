class TwoPointers:
    # for sorted array
    @staticmethod
    def find_pair_with_given_sum(arr: list, target_sum: int):
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] + arr[j] == target_sum:
                return True
            elif arr[i] + arr[j] > target_sum:
                j -= 1
            else:
                i += 1
        return False


print(TwoPointers().find_pair_with_given_sum([1, 2, 3, 4, 5], 3))
