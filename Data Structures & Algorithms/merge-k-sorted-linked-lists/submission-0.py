# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        if len(lists) % 2 != 0:
            lists.append(None)
        
        mergedLists = deque(lists)
        while len(mergedLists) != 1:
            n = len(mergedLists)
            for i in range(n // 2):
                merged = self.merge2Lists(mergedLists.popleft(), mergedLists.popleft())
                mergedLists.append(merged)
        return mergedLists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l2 is None else l2
        return dummy.next

