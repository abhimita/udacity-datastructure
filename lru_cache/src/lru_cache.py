
import unittest
import sys

"""
Node for doubly linked list
"""
class Node:
    def __init__(self, key, value):
        self.key = key     # instance variable to hold the key
        self.value = value # instance variable to hold value
        self.next = None   # forward pointer for doubly linked list
        self.prev = None   # backward pointer for doubly linked list

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def __str__(self):
        return str(self.key) + ':' + self.value


"""
Doubly linked list to keep track of usage of cache entries
Cache entry gets pushed to the front of the doubly linked list as they get created
When the entry is accessed it is brought to the front of the linked list 
unless it is in the front of the queue already
At any time element in the front is the most recently accessed entry
When cache is filled and a new key needs to be inserted the last element of the doubly linked list is removed
as this is the least recently used element
"""
class UsageList:
    def __init__(self):
        self.head = None
        self.tail = None

    """
    Insert at the front of the doubly linked list
    Parameter: n - element that needs to be inserted to the linked list
    Returns the value of the key
    """
    def insert(self, n):
        if self.head is None:
            # If this is the first node then initialize head and tail pointer to pint to this node
            self.head = self.tail = n
        else:
            # Otherwise only head pointer needs to be manipulated
            self.head.prev = n
            n.next = self.head
            self.head = n
        return n.get_value()

    """
    Remove the last element pointed by tail pointer
    This element is the one which is least recently used
    Returns the key fo the element purged from cache
    """
    def remove(self):
        if self.tail is not None:
            oldest_key = self.tail.key
            self.tail = self.tail.prev
            if self.tail is None:
                # This was the only element. After removal, doubly linked list is empty
                # tail pointer is already set to None
                # Do the same for head pointer as well
                self.head = self.tail
            else:
                # Otherwise adjust the next pointer of the element before the one that is removed
                # Set the next pointer of this node to none
                self.tail.next = None
            return oldest_key
        else:
            # If the doubly linked list is empty then there is nothing to remove
            # raise exception in that case
            raise Exception("Invalid remove operation when list is empty")

    """
    When an element is accessed this method brings the element to the front of the list
    That way we keep track of of aging of the elements
    Parameter: n - element that needs to be brought to front of the list
    Returns the value of the element which is moved to front
    
    """
    def bring_to_front(self, n):
        if self.head != n: # This is the front of cache
            n.prev.next = n.next
            if n.next is not None:
                n.next.prev = n.prev
            n.prev = None
            self.insert(n)
        return n.get_value()

    """
    Helper generator utility to traverse the doubly linked list
    Parameter:
    value: True returns the values in order of recency of use (most recent to least)
           False returns the keys in order of recency of use (most recent to least)
    """
    def dump(self, value=True):
        ptr = self.head
        while ptr is not None:
            data = ptr.get_value() if value else ptr.get_key()
            ptr = ptr.next
            yield data

"""
Class implementing LRU cache
"""
class LRU_Cache(object):
    def __init__(self, capacity):
        self.cache = {}          # Dictionary used to store key and reference to cache entry in doubly linked list
        self.capacity = capacity # Max capacity of the cache
        self.size = 0            # Current size of the cache
        self.usage = UsageList()
    """
    Method to get cache entry given the key. Accessing the element also brings the entry to the front of the queue
    Arguments:
      key: key to access the cache entry
    Returns:
      -1 : if the entry with key is not found
      otherwise return the value associated with key 
    """
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        n = self.cache.get(key, None)
        if n is not None: # Item is used
            # Insert accessed key at the front of the list
            return self.usage.bring_to_front(n)
        else:
            return -1

    """
    Method to create a cache entry. It creates an entry if key is not there in cache
    Otherwise it does not do anything (as per the given spec)
    During insertion, if the cache is already full it removes the least recently used entry
    
    Arguments:
      key: key of the cache entry
      value: value associated with key
    Returns:
      The method has side effect as it modifies the data structures. It doesn't return anything.
    """
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.size < self.capacity:
            if self.get(key) == -1:
                n = Node(key, value)
                self.cache[key] = n
                self.usage.insert(n)
                self.size += 1
            else:
                # No action is needed as the instruction states that "Set the value if the key is not present in the cache"
                # In this case the key is present. So even if `value` is different we don't update to comply with specification
                pass
        else:
            oldest_key = self.usage.remove()
            self.cache.pop(oldest_key)
            n = Node(key, value)
            self.cache[key] = n
            self.usage.insert(n)


"""
Unit testing class for LRU cache
"""

class Test_LRU_Cache(unittest.TestCase):

    def setup(self, capacity):
        return LRU_Cache(capacity)

    # Two elements are copied to cache and the second one is accessed. Cache is not full.
    def test_get_element_when_cache_not_full(self):
        # Max cache size is 5
        lru_cache = self.setup(5)
        # Two key & value pairs are put in cache
        # Cache is not full till now
        for i in [1, 2]:
            lru_cache.set(i, "data-%d" % i)
        self.assertEqual(lru_cache.capacity, 5)
        self.assertEqual(lru_cache.size, 2)
        print "lru_cache.get(2)"
        # Expected data-2
        data = lru_cache.get(2)
        self.assertEqual(data, "data-2")

    # Cache is empty and attempt to access an element by key should return -1 (edge case)
    def test_get_element_when_cache_empty(self):
        lru_cache = self.setup(5)
        self.assertEqual(lru_cache.capacity, 5)
        self.assertEqual(lru_cache.size, 0)
        data = lru_cache.get(2)
        print "lru_cache.get(2)"
        # Expected -1
        self.assertEqual(data, -1)

    # Five elements were copied to cache. After that cache is full (edge_case)
    # Attempt to put 4th element will result in LRU element being thrown out
    # Accessing 4th element should give back the value associated with 4th element
    def test_set_element_when_cache_is_full(self):
        # Max cache size is 5
        lru_cache = self.setup(5)
        # Three key & value pairs are put in cache
        for i in [1, 2, 3, 4, 5]:
            lru_cache.set(i, "data-%d" % i)
        self.assertEqual(lru_cache.capacity, 5)
        self.assertEqual(lru_cache.size, 5)
        # Fourth element is written to cache. This will age out one of the elements
        # Element (1, "data-1") is the least used element. That should get dropped off
        lru_cache.set(6, "data-6")
        data = lru_cache.get(6)
        print("lru_cache.get(6)")
        # Expected data-6
        # Cache now should contain following keys [4, 3, 2]
        self.assertEqual(data, "data-6")
        data = lru_cache.get(1)
        print("lru_cache.get(1)")
        # Expected -1
        self.assertEqual(data, -1)
        for i in [2, 3, 4]:
            data = lru_cache.get(i)
            self.assertEqual(data,"data-%d" % i)

    # Five elements were moved to cache. After that cache is full (edge case)
    # Attempt to put 4th element will result in LRU element being thrown out
    # Confirm the order of the elements in cache: keys in order are [4, 3, 2]
    def test_lru_purged_when_cache_is_full(self):
        lru_cache = self.setup(5)
        # Three key & value pairs are put in cache
        for i in [1, 2, 3, 4, 5]:
            lru_cache.set(i, "data-%d" % i)
        lru_cache.get(2)
        lru_cache.get(3)
        # Least recently used element is with key = 1
        lru_cache.set(6, "data-6")
        # Cache contains elements with following keys in this order [4, 3, 2]
        cache_keys = [k for k in lru_cache.usage.dump(value=False)]
        self.assertEqual(cache_keys, [6, 3, 2, 5, 4])
        self.assertEqual([k for k in lru_cache.usage.dump()], ['data-6', 'data-3', 'data-2', 'data-5', 'data-4'])
        # Element with key = 1 has been purged from cache
        self.assertTrue(1 not in cache_keys)
        data = lru_cache.get(-1)
        print("lru_cache.get(-1)")
        # Expected -1

if __name__ == '__main__':
    unittest.main()

