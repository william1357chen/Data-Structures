# Simple SinglyLinkedList class 

class SinglyLinkedList:
    class Node:
        def __init__(self, data = None):
            self.next = None
            self.data = data
    
    def __init__(self, head = None):
        self.head = head
    
    def append(self, data):
        if self.head is None:
            self.head = self.Node(data)
            return 

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = self.Node(data)
        return 
    def remove(self, data):
        if self.head is None:
            raise Exception("Linked List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return data

        node = self.head
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
                return data
            node = node.next
        else:
            raise KeyError
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next
        
def test():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.remove(1)
    sll.remove(3)
    for num in sll:
        print(num)
    
    
if __name__ == "__main__":
    test()