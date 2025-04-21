"""
Given two binary strings a and b, return their sum as a binary string.
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            number_a = int(a[i]) if i >= 0 else 0
            number_b = int(b[j]) if j >= 0 else 0

            total = number_a + number_b + carry
            carry = total // 2

            i = i - 1
            j = j - 1

            if total == 0:
                res.append(str(total))
            elif total == 1:
                res.append(str(total))
            elif total == 2:
                res.append("0")
            elif total == 3:
                res.append("1")

        return ''.join(res[::-1])


if __name__ == '__main__':
    s = Solution()
    a_x = '11'
    b_x = '1'
    print(s.addBinary(a_x, b_x))

    a_y = '1010'
    b_y = '11'
    print(s.addBinary(a_y, b_y))
