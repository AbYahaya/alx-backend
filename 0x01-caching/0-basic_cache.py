#!/usr/bin/env python3
"""
This file contins a class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class - a caching system that doesn't have a limit
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value
        for the key 'key'. If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or the key doesn't exist, return None.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
