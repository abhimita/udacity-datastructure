import unittest
from lru_cache import LRU_Cache
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
        # Expected data-2
        data = lru_cache.get(2)
        self.assertEqual(data, "data-2")

    # Cache is empty and attempt to access an element by key should return -1 (edge case)
    def test_get_element_when_cache_empty(self):
        lru_cache = self.setup(5)
        self.assertEqual(lru_cache.capacity, 5)
        self.assertEqual(lru_cache.size, 0)
        data = lru_cache.get(2)
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
        # Expected data-6
        # Cache now should contain following keys [4, 3, 2]
        self.assertEqual(data, "data-6")
        data = lru_cache.get(1)
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
        # Expected -1
        self.assertEqual(data, -1)

if __name__ == '__main__':
    unittest.main()

