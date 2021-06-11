class Item:
    def __init__(self, priority, value=None):
        self.priority = priority
        self.value = value

    # Allows for the syntax item1 < item2
    def __lt__(self, other):
        return self.priority < other.priority
class MinHeap: 
    def __init__(self, ) -> None:
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def left_idx(self, i):
        return 2 * i + 1

    def right_idx(self, i):
        return 2 * i + 2
    
    def parent_idx(self, i):
        return (i - 1) // 2
    
    def has_left(self, i):
        return self.left_idx(i) < len(self.data)

    def has_right(self, i):
        return self.right_idx(i) < len(self.data)
    
    def min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        return self.data[0]
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def insert(self, priority, value = None):
        self.data.append(Item(priority, value))
        self.bubble_up(len(self.data) - 1)
    
    def bubble_up(self, i):
        if i == 0:
            return 
        else:
            parent = self.parent_idx(i)
            if self.data[i] < self.data[parent]:
                self.swap(i, parent)
                self.bubble_up(parent)

        """
        # Iteratively:
        while i > 0:
            parent = self.parent_idx(i)
            if self.data[i] < self.data[parent]:
                self.swap(i, parent)
                i = parent
            else:
                return  
        """

    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        self.swap(0, -1)
        item = self.data.pop()
        if not self.is_empty():
            self.bubble_down(0)
        return item
    
    def bubble_down(self, i):
        if not self.has_left(i) and not self.has_right(i):
            # has no children
            return
        elif self.has_left(i) and not self.has_right(i):
            # only has left child
            min_child_idx = self.left_idx(i)
        else:
            # has two children
            left = self.left_idx(i)
            right = self.right_idx(i)
            min_child_idx = left if self.data[left] < self.data[right] else right
        
        if self.data[min_child_idx] < self.data[i]:
            self.swap(i, min_child_idx)
            self.bubble_down(min_child_idx)

# Time Complexity: O(nlogn) Space Complexity: O(n)
# Not the traditional heap sort
def heap_sort(lst):
    heap = MinHeap()
    for elem in lst:
        heap.insert(elem)
    sorted_lst = []
    while not heap.is_empty():
        item = heap.delete_min()
        sorted_lst.append(item.priority)
    return sorted_lst

    