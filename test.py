
class Node:
    def __init__(self):
        self.value = None

class Tree:
    def __init__(self):
        self.root = Node()

    def test(self, root):
        root.value = 1

hi = Tree()
print(hi.root.value)
hi.test(hi.root)
print(hi.root.value)