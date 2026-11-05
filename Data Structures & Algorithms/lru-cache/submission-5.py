class ListNode:
    def __init__(self, value = 0, key = 0, prev = None, nxt = None):
        self.value = value
        self.key = key
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.left_dummy = ListNode()
        self.right_dummy = ListNode()
        self.left_dummy.nxt = self.right_dummy
        self.right_dummy.prev = self.left_dummy
        self.capacity = capacity
        self.used = 0

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        cur = self.d[key]
        value = cur.value
        self.remove(cur)
        self.insert_left(cur)

        return value

    def remove(self, node):
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt

    def insert_left(self, node):
        node.nxt = self.left_dummy.nxt
        node.prev = self.left_dummy
        node.prev.nxt = node
        node.nxt.prev = node
        
    def put(self, key: int, value: int) -> None:
        print(f"put{key},{value}")
        if key in self.d:
            self.d[key].value = value
            self.remove(self.d[key])
            self.insert_left(self.d[key])
            return 

        if self.used + 1 > self.capacity:
            evict = self.right_dummy.prev
            print(evict.key, evict.value)
            del self.d[evict.key]
            self.remove(evict)
            del(evict)
            self.used -= 1

        self.used += 1

        new = ListNode(value, key)
        self.d[key] = new
        self.insert_left(new)



            

