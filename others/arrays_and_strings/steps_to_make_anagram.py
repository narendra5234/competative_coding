class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)
        min_steps = 0
        for char, value in s_counter.items():
            if value > t_counter[char]:
                min_steps += value - t_counter[char]
        return min_steps


print(Solution().minSteps("leetcode", "practice"))
