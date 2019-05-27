
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
class LRUCache(object):
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


