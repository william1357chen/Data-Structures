from DoublyLinkedList import DoublyLinkedList
import random
class Item:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

# Coding Funciton: python's built-in coding function, work with immutables
# Compression Function: Multiply-Add-and-Divide Method h(k) = [(ak + b) mod p] mod N
# Let p be prime number bigger than the biggest key we'll see
# Let a be a random number between {1, 2, ..., p - 1}
# Let b be a random number between {0, 1, ..., p - 1}
# N is the number of buckets
class ChainingHashMap:
    def __init__(self, N = 64, p = 40206835204840513073):
        self.size = 0
        self.table_size = N
        self.table = [DoublyLinkedList() for _ in range(self.table_size)]
        self.p = p
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
            
    def hash_function(self, key):
        return ((self.a * hash(key) + self.b) % self.p) % self.table_size
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self)

    def find_node(self, key, bucket):
        curr_node = bucket.head.next
        while curr_node is not bucket.trail:
            if curr_node.data.key == key:
                return curr_node
            curr_node = curr_node.next
        return None

    def __getitem__(self, key):
        idx = self.hash_function(key)
        node = self.find_node(key, self.table[idx])
        if node is None:
            raise KeyError("{} is not in the map".format(key))
        else:
            return node.data.value

    def __setitem__(self, key, value):
        idx = self.hash_function(key)
        node = self.find_node(key, self.table[idx])
        if node is None:
            new_item = Item(key, value)
            self.table[idx].append(new_item)
            self.size += 1
        else:
            node.data.value = value

        if self.size >= self.table_size:
            self.rehash(2 * self.table_size)

    def __delitem__(self, key):
        idx = self.hash_function(key)
        node = self.find_node(key, self.table[idx])
        if node is None:
            raise KeyError("{} is not in the map".format(key))
        else:
            self.table[idx].delete_node(node)

    def __iter__(self):
        for curr_llist in self.table:
            for curr_item in curr_llist:
                yield curr_item.key

    def rehash(self, new_size):
        old_table = self.table
        self.table_size = new_size
        self.table = [DoublyLinkedList() for _ in range(self.table_size)]

        for bucket in old_table:
            for item in bucket:
                new_idx = self.hash_function(item.key)
                new_bucket = self.table[new_idx]
                new_bucket.append(item)
    

def test():
    hash_map = ChainingHashMap()
    hash_map["will"] = 19
    hash_map["ben"] = 21
    hash_map["grace"] = 40
    for key in hash_map:
        print(key, end=" ")
    print(hash_map["will"])
    del hash_map["will"]
    for key in hash_map:
        print(key, end=" ")

if __name__ == "__main__":
    test()