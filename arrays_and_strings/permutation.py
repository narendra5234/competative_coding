from typing import List


class Permutation:
    def get_permutation(self, arr: List[int]):
        start, end = 0, len(arr) - 1
        return self._permutate(arr, start, end)

    def _permutate(self, arr, start, end):
        res = []
        if start == end:
            # import copy use deepcopy
            return [arr[:]]
        for index in range(start, end + 1):
            arr[index], arr[start] = arr[start], arr[index]
            res.extend(self._permutate(arr, start + 1, end))
            arr[index], arr[start] = arr[start], arr[index]
        return res

    @staticmethod
    def get_permutation_2(nums):
        perms = [[]]
        for each_num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [each_num] + perm[i:])  ###insert n
            perms = new_perms
        return perms

    @staticmethod
    def get_permutation_3(nums):
        from itertools import permutations
        return list(permutations(nums))


print(Permutation().get_permutation_3([1, 2, 3]))
