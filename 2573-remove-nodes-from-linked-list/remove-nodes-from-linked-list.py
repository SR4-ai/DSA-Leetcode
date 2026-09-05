# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        stack=[]

        while curr:
            while stack and curr.val>stack[-1].val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        stack[-1].next = None

        return stack[0]
        

                
                






