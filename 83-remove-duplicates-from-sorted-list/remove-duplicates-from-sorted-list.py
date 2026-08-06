# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        prev = head
        curr = head.next

        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head



        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    ''' off = head[0]
        cm = head[1]
        uni = 1
        while(cm<len(head)):
            if head[cm]==head[cm-1]:
                cm+=1
                continue
            head[off+1]= head[cm]
            off+=1
            uni+=1
            cm+=1
        return uni'''

        