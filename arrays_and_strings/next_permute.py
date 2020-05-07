from typing import List


class NextPermutation:
    @staticmethod
    def next_permutation(arr: List[int]):
        if arr == sorted(arr, reverse=True):
            arr.sort()
            print(arr)
        else:
            dec_index = len(arr) - 2
            while dec_index >= 0 and arr[dec_index + 1] <= arr[dec_index]:
                dec_index -= 1
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = arr[i + 1:][::-1]
            print(arr)
            return True


NextPermutation().next_permutation([3, 2, 1])
