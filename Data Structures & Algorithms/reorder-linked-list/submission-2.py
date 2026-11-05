# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        pre = None
        cur = slow.next
        slow.next = None

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt



        l = head
        r = pre



        while r :
            l_next = l.next
            r_pre = r.next
            l.next = r
            r.next = l_next
            l = l_next
            r = r_pre
        

