"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []
        stack = []
        current = root

        # пока есть узлы или то, что прошли
        while current or len(stack) > 0:
            while current:
                # собираем то, где были
                stack.append(current)
                # идем налево
                current = current.left

            # вытаскиваем последнее из прошедшего
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result