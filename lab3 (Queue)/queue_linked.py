
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.back = None
        self.num_items = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError

        if self.num_items == 0:
            node = Node(item)
            node.next = None
            self.front = node
            self.back = node
            self.num_items += 1
        else:
            node = Node(item)
            node.next = None
            self.back.next = node
            self.back = node
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError

        x = self.front.item
        self.front = self.front.next
        self.num_items -= 1
        return x


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
