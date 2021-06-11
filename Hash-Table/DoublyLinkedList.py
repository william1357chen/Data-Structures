class DoublyLinkedList:
    class Node:
        def __init__(self, prev = None, next = None, data = None):
            self.next = next
            self.prev = prev
            self.data = data

    def __init__(self, head = None, trail = None):
        self.head = self.Node()
        self.trail = self.Node()
        self.head.next = self.trail
        self.trail.prev = self.head
    
    def append(self, data):
        node = self.Node(self.trail.prev, self.trail, data)
        self.trail.prev.next = node
        self.trail.prev = node

    def appendleft(self, data):
        node = self.Node(self.head, self.head.next, data)
        self.head.next.prev = node
        self.head.next = node

    def pop(self):
        if self.trail.prev is None:
            raise KeyError
        data = self.trail.prev.data 
        self.trail.prev.prev.next = self.trail
        self.trail.prev = self.trail.prev.prev
        return data

    def popleft(self):
        if self.head.next is None:
            raise KeyError
        data = self.head.next.data
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return data

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        data = node.data
        return data

    def __iter__(self):
        node = self.head.next
        while node is not self.trail:
            yield node.data
            node = node.next
        

def test():
    dll = DoublyLinkedList()
    dll.append(2)
    dll.appendleft(1)
    dll.append(3)
    for num in dll:
        print(num)
    dll.pop()
    dll.popleft()
    for num in dll:
        print(num)


if __name__ == "__main__":
    test()