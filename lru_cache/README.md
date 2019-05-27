# Introduction

This is an implementation of Least Recently Used cache using Python data structures. The `cache` class has two methods.

1. `get`: While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss. In case of a cache hit, get() operation should return the appropriate value. In case of a cache miss, your get() should return -1.

2. `set`: There is a maximum cache size. If the cache is full and attempt is made to insert a new entry, least recently used element from cache needs to be purged.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5
## Directory organization

There are two directories. 
1. `src` - contains the source code for LRU cache implementation
2. `test` - contains the unit test cases. It uses Python's `unittest` module

## Execution

To execute the code from command line, following steps are needed.

1. `cd <directory where code is checked out>`
2. `PYTHONPATH=lru_cache/src python lru_cache/test/test_lru_cache.py`

### Output
```
test_get_element_when_cache_empty (__main__.TestLRUCache) ... ok
test_get_element_when_cache_not_full (__main__.TestLRUCache) ... ok
test_lru_purged_when_cache_is_full (__main__.TestLRUCache) ... ok
test_set_element_when_cache_is_full (__main__.TestLRUCache) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## Code design

LRU cache implementation includes two data structures.

- Dictionary (hash) storing the key and pointer to actual node in doubly linked list (see next)
- Doubly linked list implementing queue structure where additions are made at the front of the queue and removal happens from 
the end.

Dictionary is used as it provides O(1) time efficiency when accessed using `key`. Time complexity of O(1) is the requirement in the specification. Along with O(1), there is a need to keep track of aging history of elements. That is taken care of by the doubly linked list. A singly linked list would have given a time complexity of O(m) for removal of arbitrary element and adding it back to the front of the list where m is the number of elements of the linked list. Doubly linkedin list is used to achieve time complexity of O(1)

When `get` method is invoked using `key` then the dictionary is looked up first. The lookup can either succeed or fail. 

- If the key is not found then `-1` is returned
- If the key is found then `value` "pointer" in the dictionary is used to retrieve the node in the doubly linked list. The node is removed from the linked list and put to the front so that it is treated as most recently used entry. removal of the node from its location in the linked list and adding it back to the front is possible in O(1) because it is a doubly linked list.

When `set` method is invoked then first dictionary is looked up for presence of `key`. If it is found then no action is taken. Otherwise if the cache is not full then a new node is created added to the begining of the list and an entry in the dictionary is created with `key` and pointer to newly created node.

If the cache is already at maximum capacity, then oldest entry is removed from the doubly linked list by adjust the pointers and `tail` of the list. `key` for the LRU element is purged from dictionary. Newly created element is added to the front of the list and dictionary.

## Efficiency

### Time efficiency

`get`: Given `key` the lookup in dictionary is of complexity O(1) whether the lookup is a success or failure. Successful lookup requires additional operation of brining the entry to the front of the list. For doubly linked list removal and re-insertion to front is also O(1) time. So overall time complexity is O(1)

`set`: Set method requires a lookup in the dictionary. If `key` is found then no action is taken. Otherwise a new entry is created with `(key, value)` and inserted to the front of the doubly linked list. That is of complexity O(1). Dictionary entry is created for `key` and having a value as pointer to the newly created entry. Overall complexity is O(1) in this case.

If the cache is already full, then there is a need to remove the last entry of the linked list as that is the LRU item. The tail pointer of linked list gives O(1) time complexity to find this element. Removal of this entry and insertion of newly created node has total of constant time complexity or O(1)

### Space Complexity

If the cache has maximum size of m, then dictionary is of O(m). This also means when cache is full then the linked list has O(m) entries. In addition to that there is need of storing `head` & `tail` pointers of the linked list. So the overall space complexity is O(m).
