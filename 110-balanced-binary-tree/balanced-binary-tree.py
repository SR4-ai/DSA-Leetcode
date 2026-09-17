# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(node):

            if node is None:
                return 0

            left = height(node.left)

            if left == -1:
                return -1

            right = height(node.right)

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1



'''
class Solution(object):
    def isBalanced(self, root):

        if root is None:
            return True

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        diff = abs(left_depth - right_depth)

        if diff > 1:
            return False

        return (
            self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def maxDepth(self, root):

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
'''