class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        dic = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = deque()
        for each in s:
            if not stack:
                stack.append(each)
            elif dic[stack[-1]] == each:
                stack.pop()
            else:
                stack.append(each)
        if not stack:
            return True
        return False


print(Solution().isValid("{[]}"))
