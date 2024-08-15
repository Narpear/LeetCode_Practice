class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}     # key : ptr to node

        # left : Least Recently Used, right : Most Recently Used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # remove node from list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # insert node at back (most recently used)
    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev_node


    def get(self, key: int) -> int:
        if key in self.cache:
            # update dll
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
            
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            # evict the LRU node from the dll and also from the cache (hashmap)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)