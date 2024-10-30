#!/usr/bin/env python3
"""FIle about east recnty used caching algorithm
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """Initialize the class by calling the parent constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign the item value to the dictionary self.cache_data for the key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Move the key to the end to show it was recently used
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Least recently used is the first item in OrderedDict
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)

    def get(self, key):
        """Return the value linked to key in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        
        # Move the key to the end to show it was recently used
self.cache_data.move_to_end(key)
        return self.cache_data[key]
