from typing import List


class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        res = [[matrix[j][i] for j in range(len(matrix))] for i in range(
            len(matrix[0]))]
        matrix = res
        for i in range(len(matrix)):
            right, left = 0, len(matrix[0]) - 1
            while right < left:
                matrix[i][right], matrix[i][left] = matrix[i][left], matrix[
                    i][right]
                right += 1
                left -= 1

        print(matrix)


Solution().rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
