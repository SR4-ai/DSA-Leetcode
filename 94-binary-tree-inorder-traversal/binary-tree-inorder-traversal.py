# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = []

        def inorder_Traversal(node):

            if node is None:
                return

            inorder_Traversal(node.left)
            answer.append(node.val)
            inorder_Traversal(node.right)

        inorder_Traversal(root)

        return answer