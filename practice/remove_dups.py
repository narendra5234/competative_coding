from typing import List


class Solution:
    @staticmethod
    def remove_dups_from_sorted(nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1

    @staticmethod
    def remove_element(nums: List[int], val: int):
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


print(Solution().remove_element([3, 2, 2, 3], 3))
