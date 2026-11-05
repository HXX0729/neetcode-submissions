"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        old = head
        old_to_new = {}
        while old:
            new = Node(old.val)
            old_to_new[old] = new
            old = old.next
        
        for old, new in old_to_new.items():
            new.next = old_to_new[old.next] if old.next else None
            new.random = old_to_new[old.random] if old.random else None

        return old_to_new[head]