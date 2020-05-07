from typing import List


class Solution:
    @staticmethod
    def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
        h = [0] * 101

        for num in nums:
            h[num] += 1

        prev = 0
        for i, num in enumerate(h):
            if num != 0:
                h[i] = prev
                prev += num

        return [h[num] for num in nums]

print(Solution().smallerNumbersThanCurrent([8,5,2,2,3]))