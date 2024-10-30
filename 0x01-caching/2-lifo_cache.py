#!/usr/bin/python3
""" LIFO Cache module that inherits from BaseCaching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class - a caching system with LIFO eviction policy """

    def __init__(self):
        """ Initialize the class and call the parent __init__ """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO policy. If the number of items
        exceeds MAX_ITEMS, discard the last item added to the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            else:
                self.cache_order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.cache_order.pop()
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key, None)
