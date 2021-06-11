from __future__ import annotations
from typing import Optional
from ArrayQueue import ArrayQueue

class Item:
    def __init__(self: Item, key: int, value: Optional[int] = None) -> None:
        self.key = key 
        self.value = value


class Node:
    def __init__(self: Node, item: Item) -> None:
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
    
    def num_children(self: Node) -> int:
        count = 0
        if (self.left is not None):
            count += 1 
        if (self.right is not None):
            count += 1
        return count
    def disconnect(self: Node) -> None:
        self.item = None
        self.parent = None
        self.left = None
        self.right = None

# Assumptions: all keys inserted are unique

class BinarySearchTree:
    # Start of Tree Class            
    def __init__(self: BinarySearchTree, root: Optional[Node] = None) -> None:
        self.root = root
        self.size = 0
    def __len__(self: BinarySearchTree) -> int:
        return self.size
    def is_empty(self: BinarySearchTree) -> bool:
        return len(self) == 0
    
    def search(self: BinarySearchTree, key: int) -> Optional[Node]:
        curr_node = self.root
        while curr_node is not None:
            if (key == curr_node.item.key):
                return curr_node
            elif (key < curr_node.item.key):
                curr_node = curr_node.left
            elif (key > curr_node.item.key):
                curr_node = curr_node.right
        return None

    def insert(self: BinarySearchTree, key: int, value: int) -> None:
        new_item = Item(key, value)
        new_node = Node(new_item)
        # if tree is empty
        if self.is_empty():
            self.root = new_node
            self.size = 1
            return 

        # search place to insert
        next_node = self.root
        while next_node is not None:
            curr_node = next_node
            if key < next_node.item.key:
                next_node = next_node.left
            elif key > curr_node.item.key:
                next_node = next_node.right
        # insert the node        
        if (key < curr_node.item.key):
            curr_node.left = new_node
        elif (key > curr_node.item.key):
            curr_node.right = new_node
        new_node.parent = curr_node
        self.size += 1

    def delete_node(self: BinarySearchTree, node: Node) -> None:
        num_children = node.num_children()
        parent = node.parent
        if num_children == 0:
            if node is parent.left:
                parent.left = None
            elif node is parent.right:
                parent.right = None
            node.disconnect()
            self.size -= 1 
        elif num_children == 1:
            if node.left is not None:
                child = node.left
            else: # node.right is not None:
                child = node.right

            if node is parent.left:
                parent.left = child
            elif node is parent.right:
                parent.right = child
            
            child.parent = parent
            node.disconnect()
            self.size -= 1 
        elif num_children == 2:
            max_of_left_subtree = self.subtree_max(node.left)
            node.item = max_of_left_subtree.item
            self.delete_node(max_of_left_subtree)

    def subtree_max(self, root):
        if root.right is None:
            return root
        else:
            return self.subtree_max(root.right)
        """
        # Iteratively:
        curr_node = root
        while curr_node.right is not None:
            curr_node = curr_node.right
        return curr_node
        """
        
    # Allows for syntax: m[k] (returns the value associated with key k)
    def __getitem__(self: BinarySearchTree, key: int) -> int:
        node = self.search(key)
        if node is None:
            raise KeyError("{} is not in the tree".format(key))
        else:
            return node.item.value
    # Allows for syntax: m[key] = val (associates key `key` with value `val`)
    def __setitem__(self: BinarySearchTree, key: int, value: int) -> None:
        node = self.search(key)
        if node is None:
            self.insert(key, value)
        else:
            node.item.value = value

    # Allows for the syntax 'del map[key]'
    def __delitem__(self: BinarySearchTree, key: int) -> None:
        node = self.search(key)
        if node is None:
            raise Exception("{} is not in the tree".format(key))
        else:
            self.delete_node(node)
    
    def preorder(self: BinarySearchTree):
        yield from self.subtree_preorder(self.root)
    def subtree_preorder(self: BinarySearchTree, root: Node) -> int:
        if root is not None:
            yield root.item.key
            yield from self.subtree_preorder(root.left)
            yield from self.subtree_preorder(root.right)

    def inorder(self: BinarySearchTree):
        yield from self.subtree_inorder(self.root)
    def subtree_inorder(self: BinarySearchTree, root: Node) -> int:
        if root is not None:
            yield from self.subtree_inorder(root.left)
            yield root.item.key
            yield from self.subtree_inorder(root.right)
            
    def postorder(self: BinarySearchTree):
        yield from self.subtree_postorder(self.root)
    def subtree_postorder(self: BinarySearchTree, root: Node) -> int:
        if root is not None:
            yield from self.subtree_postorder(root.left)
            yield from self.subtree_postorder(root.right)
            yield root.item.key

    def breath_first(self: BinarySearchTree):
        queue = ArrayQueue()
        queue.enqueue(self.root)

        while queue.is_empty() is not True:
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            yield node.item.key

def test():
    tree = BinarySearchTree()
    tree[2] = None
    tree[1] = None
    tree[3] = None
    print(tree.size)
    for key in tree.preorder():
        print(key, end=" ")
    print()
    del tree[3]
    for key in tree.breath_first():
        print(key, end=" ")
    print()
    print(tree[2])

if __name__ == "__main__":
    test()