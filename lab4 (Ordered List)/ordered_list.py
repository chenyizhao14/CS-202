class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dummy.next is self.dummy

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance.  Assume that all items added to your
           list can be compared using the < operator and can be compared for equality/inequality.
           Make no other assumptions about the items in your list'''
        # base case: empty
        node = Node(item)
        now = self.dummy.next
        if now.item == node.item:
            return False
        # comparing until we get to less than
        while now is not self.dummy and now.item < node.item:
            now = now.next
            if node.item == now.item:
                return False

        # when now is greater than node
        # things that need to be changed: now.prev's next, now's prev, node.next, node.prev,
        now.prev.next = node
        node.prev = now.prev
        now.prev = node
        node.next = now
        return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        now = self.dummy.next
        while now is not self.dummy:
            if now.item != item:
                now = now.next
                continue
            now.prev.next = now.next
            now.next.prev = now.prev
            return True

        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        # the head is index 0
        now = self.dummy.next
        index = 0
        while now is not self.dummy:
            if now.item == item:
                return index

            now = now.next
            index += 1
        # finished through loop, can't find the index of the item
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0:
            raise IndexError()

        now = self.dummy.next
        i = 0

        # when the index is not at 0, but still within range
        while (now is not self.dummy) and (i < index):
            i += 1
            now = now.next

        if now is self.dummy:
            raise IndexError()

        now.prev.next = now.next
        now.next.prev = now.prev

        return now.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(self.dummy.next, item)

    # recursive function to find the item
    def search_helper(self, node, item):
        if node.item == item:
            return True

        if node is self.dummy:
            return False

        return self.search_helper(node.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        x = self.dummy.next
        lst = []
        while x is not self.dummy:
            lst.append(x.item)
            x = x.next

        return lst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper(self.dummy.prev)

    def python_list_reversed_helper(self, node):
        # base case is when it's the dummy: returns None
        if node is self.dummy:
            return []

        return [node.item] + self.python_list_reversed_helper(node.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.dummy.next)


    def size_helper(self, node):
        # the dummy does not count as 1 because it has no data
        if node is self.dummy:
            return 0

        return 1 + self.size_helper(node.next)

