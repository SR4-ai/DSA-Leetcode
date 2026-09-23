# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def search_val(node):

            if node == None:
                return None
            if node.val == val:
                return node
            elif val<node.val:
               return search_val(node.left)
            else:
               return search_val(node.right)
        return search_val(root)