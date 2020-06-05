from typing import List


class Solution:
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while index >= 0:
            carry, digits[index] = divmod(digits[index] + carry, 10)
            index -= 1
        if carry:
            digits.insert(0, carry)
        return digits


print(Solution().plusOne([9, 9, 9]))
