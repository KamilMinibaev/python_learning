"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # множество текущих уникальных символов
        unique_symbols = set()
        max_length = 0
        # начало окна
        left = 0

        for symbol in range(len(s)):
            while s[symbol] in unique_symbols:
                unique_symbols.remove(s[left])
                left += 1

            unique_symbols.add(s[symbol])
            max_length = max(max_length, symbol - left + 1)

        return max_length


if __name__ == '__main__':
    s = Solution()
    x = "abcabcbb"
    print(s.lengthOfLongestSubstring(x))
