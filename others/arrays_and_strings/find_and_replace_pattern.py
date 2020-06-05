from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        import re
        from collections import Counter
        pattern_counter = Counter(pattern)
        regex = r""
        for char, value in pattern_counter.items():
            regex+=
