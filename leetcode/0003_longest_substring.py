"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_symbols = set()  # множество текущих уникальных символов
        max_length = 0
        left = 0                # начало окна

        for symbol in range(len(s)):
            while s[symbol] in unique_symbols:
                unique_symbols.remove(s[left])  # убираем символ слева
                left += 1                      # сдвигаем левую границу

            unique_symbols.add(s[symbol])       # добавляем новый символ
            max_length = max(max_length, symbol - left + 1)

        return max_length


if __name__ == '__main__':
    s = Solution()
    x = "abcabcbb"
    print(s.lengthOfLongestSubstring(x))
