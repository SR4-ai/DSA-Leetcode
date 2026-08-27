# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Find length
        n = 1
        curr = head

        while curr.next:
            curr = curr.next
            n += 1

        # Avoid unnecessary rotations
        k = k % n

        if k == 0:
            return head

        # Find new tail
        curr = head
        for _ in range(n - k - 1):
            curr = curr.next

        # New head
        new_head = curr.next

        # Break the list
        curr.next = None

        # Connect old tail to old head
        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head

        return new_head
            

