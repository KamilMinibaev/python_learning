"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = (begin + end) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                begin = mid + 1

            else:
                end = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    nums_x = [-1,0,3,5,9,12]
    target_x = 9
    print(s.search(nums_x, target_x))

    nums_y = [-1,0,3,5,9,12]
    target_y = 2
    print(s.search(nums_y, target_y))
