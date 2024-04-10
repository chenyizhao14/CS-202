
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False

        self.num_items += 1
        self.items[self.num_items] = item
        self.perc_up(self.num_items)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        # if there is nothing to peek at, return None
        if self.is_empty():
            return None

        # the max is the very first number
        return self.items[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        # if the heap is empty, return None
        if self.is_empty():
            return None

        # return the root, remove it, then replace with data from end of the heap
        # percolate down
        max = self.items[1]

        self.items[1] = self.items[self.num_items] # changing the max to the very last number
        self.items[self.num_items] = None # what we just put as max is changed to None
        self.num_items -= 1 # since the max got removed, the number of items decreases
        self.perc_down(1) # perc down, sorting the "max" number down to where it belongs

        # return the top priority item (max)
        return max

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        # return by iterating through and add data that is not None
        contents = []
        for i, data in enumerate(self.items):
            if data is not None:
                contents.append(self.items[i])

        return contents

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        if len(alist) > self.capacity:
            self.capacity = len(alist)
            self.items = [None] * (self.capacity + 1)

        self.num_items = len(alist)
        self.items = [None] + alist + [None]
        i = len(alist)//2

        while i > 0:
            self.perc_down(i)
            i -= 1

        return

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.num_items == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.num_items == self.capacity
        
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        # remember that the 0th index is not used
        return self.capacity
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items
        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''

        # when perking down and in most cases, there are 2 children
        while (i * 2) <= self.num_items:
            mc = self.maxChild(i)
            if self.items[i] < self.items[mc]:
                tmp = self.items[i]
                self.items[i] = self.items[mc]
                self.items[mc] = tmp
            i = mc

    # find the larger child and swap the root with the larger child
    def maxChild(self,i):
      if i * 2 + 1 > self.num_items:
          return i * 2
      else:
          if self.items[i * 2] > self.items[i * 2 + 1]:
              return i * 2
          else:
              return i * 2 + 1

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                tmp = self.items[i // 2]
                self.items[i // 2] = self.items[i]
                self.items[i] = tmp
            i = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        for i in range(len(alist) - 1, -1, -1):
            alist[i] = self.dequeue()
            # print(alist[i])
        return alist




