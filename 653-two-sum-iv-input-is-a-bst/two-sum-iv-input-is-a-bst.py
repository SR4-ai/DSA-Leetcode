# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        seen = set()
        def find(node):
            if node is None:
                return False

            else:
                diff = k - node.val
                if diff in seen:
                    return True
                else:
                    seen.add(node.val)
                return find(node.left) or find(node.right)
                

        return find(root)

            
