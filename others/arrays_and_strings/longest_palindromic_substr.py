class LPS:
    # brute force O(n2) -generating all substring
    # and check if palindrome
    def longest_palindromic_sub_str(self, string: str):
        sub_str = ""
        for i in range(len(string)):
            for j in range(i, len(string)):
                curr_sub_str = string[i:j + 1]
                if self._is_palindrome(curr_sub_str):
                    if len(curr_sub_str) > len(sub_str):
                        sub_str = curr_sub_str
        return sub_str

    @staticmethod
    def _is_palindrome(sub_str):
        return sub_str == sub_str[::-1]

    # Try to use Window Sliding Technique
    def longest_palindromic_sub_str_1(self, string: str):
        sub_str, i, j, curr_sub_str = "", 0, 0, ""
        while i < len(string) and j < len(string):
            curr_sub_str = string[i:j + 1]
            if self._is_palindrome(curr_sub_str):
                if len(sub_str) > len(curr_sub_str):
                    sub_str = curr_sub_str
                    j+=1


obj = LPS()
print(obj.longest_palindromic_sub_str("cbbd"))
