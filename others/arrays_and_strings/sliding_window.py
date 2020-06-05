import sys
from typing import List


class SlidingWindow:
    # Fixed Size k
    @staticmethod
    def max_sum_of_sub_arrays_of_length_k(arr: List[int], k: int):
        max_sum, curr_sum = -sys.maxsize, 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if i >= k - 1:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= arr[i - (k - 1)]
        return max_sum

    # Dynamic SIze Window with i as start and j as end.
    @staticmethod
    def smallest_sub_array_with_given_sum(arr: List[int], target_sum: int):
        curr_sum, i, j, min_sub = 0, 0, 0, sys.maxsize
        while i < len(arr) and j < len(arr):
            curr_sum += arr[j]
            while curr_sum >= target_sum:
                min_sub = min(min_sub, j - i + 1)
                curr_sum -= arr[i]
                i += 1
            j += 1
        return min_sub

    # Dynamic Window with HashMap especially used for strings.
    # with window start as i and  window end as j
    @staticmethod
    def longest_sub_str_with_k_distinct_chars(string: str, k: int):
        curr_dict, i, j, max_sub = {}, 0, 0, -sys.maxsize
        while i < len(string) and j < len(string):
            curr_dict[string[j]] = curr_dict.get(string[j], 0) + 1
            while len(curr_dict) > k:
                curr_dict[string[i]] = curr_dict.get(string[j]) - 1
                if curr_dict[string[i]] == 0:
                    del curr_dict[string[i]]
                i += 1
            max_sub = max(max_sub, j - i + 1)
            j += 1
        return max_sub

    # Using Hashmap
    @staticmethod
    def longest_sub_str_without_repeating_chars(string: str):
        curr_dict, i, j, max_sub = {}, 0, 0, -sys.maxsize
        while i < len(string) and j < len(string):
            if string[j] in curr_dict:
                i = max(i, curr_dict[string[j]])
            curr_dict[string[j]] = j + 1
            max_sub = max(max_sub, j - i + 1)
            j += 1
        return max_sub

    # Using HashSet
    @staticmethod
    def longest_sub_str_without_repeating_chars_1(string: str):
        curr_set, i, j, max_sub = set(), 0, 0, 0
        while i < len(string) and j < len(string):
            if string[j] in curr_set:
                curr_set.remove(string[i])
                i += 1
            else:
                curr_set.add(string[j])
                j += 1
                max_sub = max(max_sub, j - i)
        return max_sub

    @staticmethod
    def minWindow(s, t):
        if not t or not s:
            return ""
        from collections import Counter
        counter_t = Counter(t)
        unique_t_len = len(counter_t)
        l, r = 0, 0
        unique_window_len = 0
        window_counts = {}  # stores count of unique chars in curr_window
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in counter_t and window_counts[character] == counter_t[character]:
                unique_window_len += 1
            while l <= r and unique_window_len == unique_t_len:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in counter_t and window_counts[character] < counter_t[character]:
                    unique_window_len -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


obj = SlidingWindow()
# print(obj.max_sum_of_sub_arrays_of_length_k([1, 2, 3, 4, 5], 3))
# print(obj.smallest_sub_array_with_given_sum([4, 2, 2, 7, 8, 1, 2, 10], 8))
# print(obj.longest_sub_str_with_k_distinct_chars("aaahhibc", 2))
# print(obj.longest_sub_str_without_repeating_chars_1("pwwkew"))
print(obj.minWindow("ABAACBAB", "ABC"))
