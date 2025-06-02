"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # находим глубину левой и правой ветви, берем макс из них
        if not root:
            return 0

        # записываю узел и глубину
        stack = [(root, 1)]
        max_depth = 0

        # пока есть куда идти
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth

        # # через рекурсию
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
