from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        dir, res = 0, []
        while top <= bottom and left <= right:
            if dir == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
                dir = 1
            elif dir == 1:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
                dir = 2
            elif dir == 2:
                for i in range(right, left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                dir = 3
            elif dir == 3:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                dir = 0
        return res


print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
