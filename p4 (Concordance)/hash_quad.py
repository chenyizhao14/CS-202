import math
class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will 
            be used, if 11 is passed, 11 will be used.)'''
        self.table_size = table_size
        if not self.is_Prime(self.table_size):
            self.table_size = self.next_prime(table_size)
        self.key = [None] * self.table_size
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value can be anything (Object, None, list, etc.).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        # insert into index of hash key % table size
        index = self.horner_hash(key) % self.table_size
        i = 0
        replace = False
        while self.key[(index + (i ** 2)) % self.table_size] is not None:
            # if key already exists, replace
            if self.key[(index + (i ** 2)) % self.table_size][0] == key:
                replace = True
                break
            i += 1

        # 2 possible situations if self.key is not none
        self.key[(index + (i ** 2)) % self.table_size] = (key, value)

        # if it was not a replacing of data, number of items increase
        if not replace:
            self.num_items += 1

        # once load factor is greater than 0.5
        # rehash into the new table, don't forget to % by new table size
        if self.get_load_factor() >= 0.5:
            self.rehash()

    def rehash(self): # make a new everything and then reset self.stuff to it
        new_table = HashTable(self.next_prime(2 * self.table_size))

        # iterating through the old hash table to rehash into the larger table
        for key in self.key:
            if key is not None:
                new_table.insert(key[0], key[1])

        self.key = new_table.key
        self.table_size = new_table.table_size
        self.num_items = new_table.num_items

    def horner_hash(self, key):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method should not mod with the table size'''
        sum = 0
        n = min(len(key) , 8)
        for i in range(n):
            horner = 31 ** (n - 1 - i)
            sum += (ord(key[i]) * horner)

        return sum

    def is_Prime(self, n):
        # Corner cases
        if n <= 1:
            return False
        if n <= 3:
            return True

        # This is checked so that we can skip
        # middle five numbers in below loop
        if n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(5, int(math.sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True
        
    def next_prime(self, n):
        ''' Find the next prime number that is > n.'''
        if n <= 1:
            return 2

        prime = n
        found = False

        # Loop continuously until isPrime returns
        # True for a number greater than n
        while not found:
            prime = prime + 1

            if self.is_Prime(prime) is True:
                found = True

        return prime

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        index = self.horner_hash(key) % self.table_size
        i = 0
        if self.key[index] is None:
            return False
        else:
            while self.key[(index + (i ** 2)) % self.table_size] is not None:
                # if key is found, return the index
                if self.key[(index + (i ** 2)) % self.table_size][0] == key:
                    return True
                i += 1

            return False

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        index = self.horner_hash(key) % self.table_size
        i = 0
        if self.key[index] is None:
            return None
        while self.key[(index + (i ** 2)) % self.table_size] is not None:
            # if key is found, return the index
            if self.key[(index + (i ** 2)) % self.table_size][0] == key:
                return (index + (i ** 2)) % self.table_size
            i += 1

        return None
        # if it leaves while loop it is None

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        # appending all keys that are not none into new list
        keys = []
        for key in self.key:
            if key is not None:
                keys.append(key[0])

        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        index = self.horner_hash(key) % self.table_size
        i = 0
        # if it doesn't exist return None
        if self.key[index] is None:
            return None

        # best case
        if self.key[index][0] == key:
            return self.key[index][1]
        else:
            while self.key[(index + (i ** 2)) % self.table_size] is not None:
                # if key is found, return the index
                if self.key[(index + (i ** 2)) % self.table_size][0] == key:
                    return self.key[(index + (i ** 2)) % self.table_size][1]
                i += 1

            return None

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return float(self.num_items) / self.table_size
