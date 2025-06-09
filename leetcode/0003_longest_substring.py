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
        substring = ''            #set()  тут с порядком может быть трабла, строка нагляднее

        # начало окна
        max_lenght = 0

        i = 0

        while i < len(s):

            if s[i] in substring:
                substring = substring[1:]

            else:
                substring += s[i]
                max_lenght = max(len(substring), max_lenght)

                i += 1

        return max_lenght


if __name__ == '__main__':
    s = Solution()
    x = "bacda"
    print(s.lengthOfLongestSubstring(x))
