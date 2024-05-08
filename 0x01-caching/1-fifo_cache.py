#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.queue:
            self.queue.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.queue.pop(0)
            del self.cache_data[first]
            print("DISCARD: {}".format(first))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
