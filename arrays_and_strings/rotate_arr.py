from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        n = len(nums)
        for i in range(n):
            nums[i] = nums[(n - k + i) % n]
        return nums


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7],
3))
