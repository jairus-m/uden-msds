from collections import deque
import heapq

class MyStack:
    """Stack implementation based on a list"""
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        """Add element into stack"""
        self.stack.append(item)
    
    def pop(self):
        """Remove the last appended element"""
        if self.empty():
            raise IndexError("Cannot pop from empty stack")
        return self.stack.pop()
    
    def top(self):
        """Retun the first appended element"""
        if self.empty():
            raise IndexError("top from empty stack")
        return self.stack[-1]
    
    def empty(self):
        """State check"""
        return len(self.stack) == 0

    
class MyQueue:
    def __init__(self, data_type):
        self.queue = deque()
    
    def enqueue(self, item):
        """Add element to queue"""
        self.queue.append(item)
    
    def dequeue(self):
        """Remove element from queue"""
        if self.empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.queue.popleft()
    
    def front(self):
        """Returns the first element in the queue"""
        if self.empty():
            raise IndexError("No front from empty queue")
        return self.queue[0]
    
    def empty(self):
        """State check"""
        return len(self.queue) == 0

class MaxHeap:
    def __init__(self):
        self.heap = []

    def add_element(self, element):
        """
        Python module, heapq, only implements a min-heap. Therefore need to
        add the negative of the element to the heap to act like a max-heap
        """
        heapq.heappush(self.heap, -element)

    def remove_root(self):
        """
        Again since heapq only implements min-heap, removing the max root node
        involves popping the "most negative" element in this implementation.
        """
        if self.heap:
            # "most-negative" = max
            return -heapq.heappop(self.heap)
        else:
            raise IndexError("Cannot remove root from an empty heap")

    def __str__(self):
        """String representation of "sorted" heap"""
        return str(sorted([-x for x in self.heap], reverse=True))

    
if __name__ == '__main__':
    print('\nPart1: MyStack\n')
    s = MyStack()
    print(s.empty())  # True
    s.push(5)
    s.push(8)
    print(s.pop())  # 8
    s.push(3)
    print(s.empty())  # False
    print(s.top())  # 3
    print(s.pop())  # 3
    print(s.pop())  # 5
    try:
        print(s.pop())  
    except IndexError as e:
        print(e)  

    print('\nPart2: MyQueue\n')
    q = MyQueue(int)
    print(q.empty())  # True
    q.enqueue(5)
    q.enqueue(8)
    print(q.dequeue())  # 5
    q.enqueue(3)
    print(q.empty())  # False
    print(q.front())  # 8
    print(q.dequeue())  # 8
    print(q.dequeue())  # 3
    try:
        print(q.dequeue())  
    except IndexError as e:
        print(e)  

    print('\nPart3: MaxHeap\n')
    max_heap = MaxHeap()
    max_heap.add_element(100)
    max_heap.add_element(64)
    max_heap.add_element(28)
    max_heap.add_element(1)

    print("MaxHeap w/ root:", max_heap)  
    print("Removed the root!:", max_heap.remove_root())  # Removed root: 100
    print("MaxHeap w/out root:", max_heap)  # MaxHeap after removing root: [64, 28, 1]

# TERMINAL OUTPUT

# Part1: MyStack

# True
# 8
# False
# 3
# 3
# 5
# Cannot pop from empty stack

# Part2: MyQueue
# 
# True
# 5
# False
# 8
# 8
# 3
# Cannot dequeue from empty queue

# Part3: MaxHeap
# 
# MaxHeap w/ root: [100, 64, 28, 1]
# Removed the root!: 100