#!/usr/bin/python3
"""This module defines the CountedIterator class, which wraps an iterator
and keeps track of the number of items that have been iterated over.
"""


class CountedIterator:
    """An iterator wrapper that maintains a counter of elements successfully

    iterated from an underlying iterable object.
    """

    def __init__(self, iterable):
        """Initializes the CountedIterator with an iterable object

        and sets the counter to 0.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the current number of items that have been iterated."""
        return self.counter

    def __next__(self):
        """Fetches the next item from the original iterator and increments

        the counter. Raises StopIteration when no items are left.
        """
        item = next(self.iterator)
        self.counter += 1
        return item
