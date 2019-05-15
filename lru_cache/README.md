# Introduction

Here is an implementation of Least Recently Used cache using Python data structures. The `cache` class has two methods.

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

1. `cd <directory where code is checked out>/lru_cache`
2. `PYTHONPATH=src python test/test_lru_cache.py`

### Output
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## Code design

LRU cache implementation includes two data structures.

- Dictionary storing the key and pointer to actual node in doubly linked list (see below)
- Doubly linked list implementing queue structure where additions are made to the front of the queue and removal happens from 
the end.

When `get` method is invoked with `key` then the dictionary is looked up first. The lookup can either succeed or fail. 

- If the key is not found then `-1` is returned
- If the key is found then `value` "pointer" in the dictionary is used to retrieve the node in the doubly linked list. The node is removed from the linked list and put to the front so that it is treated as most recently used entry


## Efficiency

