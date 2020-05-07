class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev = 0
        num = 0
        for index in range(len(s) - 1, -1, -1):
            if map[s[index]] > prev:
                num += map[s[index]]
            else:
                num -= map[s[index]]
            prev = map[s[index]]
        return num
