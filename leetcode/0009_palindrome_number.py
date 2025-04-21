"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        initial_x = x

        if initial_x < 0:
            return False

        res = 0

        while x != 0:
            a = x % 10
            x = x // 10

            res = res * 10 + a

        return initial_x == res


if __name__ == '__main__':
    s = Solution()
    x = 121
    print(s.isPalindrome(x))

    y = -121
    print(s.isPalindrome(y))

    z = 1011
    print(s.isPalindrome(z))
