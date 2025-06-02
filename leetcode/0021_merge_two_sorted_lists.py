"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        listnode = ListNode()
        root = listnode

        while list1 and list2:
            if list1.val < list2.val:
                root.next = list1
                list1 = list1.next
            else:
                root.next = list2
                list2 = list2.next

            root = root.next

        if list1:
            root.next = list1
        else:
            root.next = list2

        return listnode.next