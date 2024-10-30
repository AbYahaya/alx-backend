#!/usr/bin/env python3
"""FIle about east recnty used caching algorithm
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a Least Recently Used caching system """

    def __init__(self):
        """ Initialize the class by calling the parent constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm """
        if key is None or item is None:
            return

        # If key exists, remove it so we can insert it again at the end
        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item  # Add key-item pair

        # If cache exceeds MAX_ITEMS, discard the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item from the cache, marking it as recently used """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
