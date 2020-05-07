from typing import List


class RemoveDuplicates:
    # preserve order
    @staticmethod
    def remove_dups_1(arr):
        b = []
        print([b.append(i) for i in arr if i not in b])

    @staticmethod
    def remove_dups_2(arr):
        from collections import OrderedDict
        print(list(OrderedDict.fromkeys(arr)))

    @staticmethod
    def remove_dups_using_sort(arr):
        b = list(set(arr))
        b.sort(key=arr.index)
        print(b)

    # doesnot preserve order
    @staticmethod
    def remove_dups(arr):
        print(list(set(arr)))

    @staticmethod
    def remove_duplicates(nums: List[int]):
        l, r = 0, 1
        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]: r += 1
            if r < len(nums):
                nums[l + 1] = nums[r]
                l += 1
                r += 1
        return l + 1


obj = RemoveDuplicates()
# obj.remove_dups([2, 3, 4, 2, 5, 4, 4, 6])
print(obj.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# ref_link: https://www.askpython.com/python/remove-duplicate-elements-from-list-python
