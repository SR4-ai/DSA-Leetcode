# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        answer = []

        def preorder_Traversal(node):

            if node is None:
                return

            answer.append(node.val)

            preorder_Traversal(node.left)
            preorder_Traversal(node.right)

        preorder_Traversal(root)

        return answer