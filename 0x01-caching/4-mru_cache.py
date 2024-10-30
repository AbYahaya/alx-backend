#!/usr/bin/env python3
"""
Implemetation of most recentlyused cache algorithm
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a Most Recently Used caching system """

    def __init__(self):
        """ Initialize the class by calling the parent constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm """
        if key is None or item is None:
            return

        # If key exists, remove it so we can insert it again at the end
        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item  # Add key-item pair

        # If cache exceeds MAX_ITEMS, discard the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        # Return the value associated with the key (no need to mark as used)
        return self.cache_data[key]
