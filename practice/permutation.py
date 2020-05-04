from typing import List


class Permutation:
    def get_permutations(self, arr: List[int]):
        start, end = 0, len(arr)-1

        return self._permutate(arr, start, end)

    def _permutate(self, arr, start, end):
        res = []
        if start == end:
            return [arr[:]]
        for _index in range(start, end+1):
            arr[_index], arr[start] = arr[start], arr[_index]
            res.extend(self._permutate(arr, start + 1, end))
            arr[_index], arr[start] = arr[start], arr[_index]
        return res

print(Permutation().get_permutations([1, 2, 3]))
