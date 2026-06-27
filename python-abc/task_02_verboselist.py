#!/usr/bin/python3
"""This module defines a custom VerboseList class that extends the built-in
list class and prints notification messages when items are modified.
"""


class VerboseList(list):
    """A custom list class that prints notifications when items are added

    using append or extend, or removed using remove or pop.
    """

    def append(self, item):
        """Adds an item to the end of the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list by appending elements from the iterable

        and prints a notification with the count of items added.
        """
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Removes the first occurrence of the specified item from the list.

        Prints a notification before removal if the item exists.
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns the item at the given index (default last).

        Prints a notification before popping the item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
