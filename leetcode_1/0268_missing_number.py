"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        for i in range(n + 1):
            if i not in nums:
                return i

        return None


if __name__ == '__main__':
    s = Solution()
    nums_x = [3 ,0, 1]
    print(s.missingNumber(nums_x))

    nums_y = [9,6,4,2,3,5,7,0,1]
    print(s.missingNumber(nums_y))
