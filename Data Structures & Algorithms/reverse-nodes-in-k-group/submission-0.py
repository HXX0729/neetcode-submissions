# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if kth is None:
                return dummy.next
            group_next = kth.next
            prev = group_prev.next
            cur = prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            tmp = group_prev.next
            tmp.next = group_next
            group_prev.next = kth
            group_prev = tmp
        
    def get_kth(self, group_prev, k):
        for i in range(k):
            if group_prev is None:
                return None
            group_prev = group_prev.next
        return group_prev

