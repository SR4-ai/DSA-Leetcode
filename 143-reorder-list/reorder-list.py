# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        # Step 2: Split
        second = slow.next
        slow.next = None

        # Step 3: Reverse second half
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # merge alternatively 
        first = head 
        second = prev 
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2