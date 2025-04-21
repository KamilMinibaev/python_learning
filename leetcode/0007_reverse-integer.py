"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x != 0:
            a = x % 10
            x //= 10
            res = res * 10 + a

        res *= sign

        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res


if __name__ == '__main__':
    s = Solution()
    x = 123
    print(s.reverse(x))

    y = 10
    print(s.reverse(y))

    z = -123
    print(s.reverse(z))
