"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def searchInsert(self, nums, target):
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

        return begin


if __name__ == '__main__':
    s = Solution()
    nums_x = [1,3,5,6]
    target_x = 5
    print(s.searchInsert(nums_x, target_x))

    nums_y = [1, 3, 5, 6]
    target_y = 2
    print(s.searchInsert(nums_y, target_y))
