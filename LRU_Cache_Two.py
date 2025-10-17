class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRU_Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}  
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToHead(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def moveToHead(self, node: Node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node_to_remove = self.tail.prev
        self.removeNode(node_to_remove)
        return node_to_remove

    def get(self, key):
        if key not in self.values:
            return -1
        node = self.values[key]
        self.moveToHead(node)
        return node.val

    def put(self, key, value):
        if key in self.values:
            node = self.values[key]
            node.val = value
            self.moveToHead(node)
        else:
            new_node = Node(key, value)
            self.values[key] = new_node
            self.addToHead(new_node)

            if len(self.values) > self.capacity:
                tail_node = self.removeTail()
                del self.values[tail_node.key]
