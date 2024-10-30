#!/usr/bin/env python3
"""
Less frequently used cache implementation
"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a Least Frequently Used caching system """

    def __init__(self):
        """ Initialize the class by calling the parent constructor """
        super().__init__()
        self.frequency = defaultdict(int)
        # OrderedDict to maintain insertion order (LRU fallback)
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item
        self.frequency[key] += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            least_freq_keys = [
                k for k in self.cache_data if self.frequency[k] == min_freq
            ]

            if len(least_freq_keys) > 1:
                lru_key = next(k for k in self.cache_data
                               if k in least_freq_keys)
            else:
                lru_key = least_freq_keys[0]

            self.cache_data.pop(lru_key)
            del self.frequency[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        return self.cache_data[key]
