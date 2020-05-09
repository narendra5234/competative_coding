from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'] }
        res = [""]
        for num in digits:
            temp = []
            if num not in keypad:
                return []
            for c in keypad[num]:
                for existing in res:
                    temp.append(existing+c)
            res = temp
        return res

print(Solution().letterCombinations("23"))
