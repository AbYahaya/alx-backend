#!/usr/bin/python3
""" FIFO Cache module that inherits from BaseCaching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class - a caching system with FIFO eviction policy """

    def __init__(self):
        """ Initialize the class and call the parent __init__ """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO policy. If the number of items
        exceeds MAX_ITEMS, discard the oldest item (first inserted).
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.cache_order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.cache_order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
