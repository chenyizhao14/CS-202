
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = None
        self.back = None

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

        if self.back == self.capacity - 1:
            self.back = 0
            self.items[self.back] = item
            self.num_items += 1
        elif not self.is_empty():
            self.items[self.back + 1] = item
            self.back += 1
            self.num_items += 1
        else:
            self.items[0] = item
            self.front = 0
            self.back = 0
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError

        if self.front == self.capacity - 1:
            x = self.items[self.front]
            self.items[self.front] = None
            self.front = 0
            self.num_items -= 1
            return x
        else:
            x = self.items[self.front]
            self.items[self.front] = None
            self.front += 1
            self.num_items -= 1
            return x

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items

