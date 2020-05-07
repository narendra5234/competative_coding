from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified, curr, curr_no = [], [], 0
        for word in words:
            if curr_no + len(word) + len(curr) > maxWidth:
                for i in range(maxWidth - curr_no):
                    curr[i % (len(curr) - 1 if len(curr) > 1 else 1)] += ' '
                justified.append(''.join(curr))
                curr, curr_no = [], 0
            curr.append(word)
            curr_no += len(word)
        return justified + [' '.join(curr).ljust(maxWidth)]


print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
