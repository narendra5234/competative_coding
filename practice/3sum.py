import sys
from typing import List


class Solution:
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = []
        for i in range(len(nums)):
            start, end = i + 1, n - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] < 0:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    triplets.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
        return triplets

    @staticmethod
    def three_sum_closest(nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_dist = sys.maxsize

        for index in range(n):
            start, end = index + 1, n - 1
            while start < end:
                curr_dist = abs(nums[index] + nums[start] + nums[end] - target)
                if curr_dist < min_dist:
                    min_dist_sum, min_dist = curr_dist + target, curr_dist

                if curr_dist < 0:
                    start += 1
                else:
                    end -= 1

        return min_dist_sum


print(Solution().three_sum([-1, 0, 1, 2, -1, -4]))
