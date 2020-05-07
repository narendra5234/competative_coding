class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        start, end, result = 0, len(needle)-1, -1

        while end <= len(haystack):
            if haystack[start] == needle:
                result = start
                break

            if haystack[start:end] == needle:
                result = start
                break
            start += 1
            end += 1