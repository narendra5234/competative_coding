from typing import List


class CountNeg:
    @staticmethod
    def count_neg(grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid))[::-1]:
            for j in range(len(grid[0]))[::-1]:
                if grid[i][j] < 0:
                    c += 1
                else:
                    break
        return c


obj = CountNeg()
print(obj.count_neg([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
