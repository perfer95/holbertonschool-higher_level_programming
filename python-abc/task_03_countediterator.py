#!/usr/bin/python3
"""
3. CountedIterator - Keeping Track of Iteration
"""


class CountedIterator():
    """ CountedIterator Class """
    def __init__(self, it):
        self.it = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.it)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        return self.count
