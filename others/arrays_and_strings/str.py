class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i, j, c=0, 0, 0
        while j<len(s):
            sub = s[i:j+1]
            if sub.count('L')!=sub.count('R'):
                j+=1
            else:
                i=j+1
                j+=1
                c+=1
        return c
print(Solution().balancedStringSplit("RLRRLLRLRL"))