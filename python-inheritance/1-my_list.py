#!/usr/bin/python3
"""This module defines a custom class named MyList that expands the built-in
list class functionality by adding specialized sorting methods.
"""


class MyList(list):
    """A custom list subclass that inherits all standard list attributes
    and introduces custom methods to display elements in a sorted manner.
    """

    def print_sorted(self):
        """Prints all elements contained within the current list instance
        sorted in ascending order without modifying the original order.
        """
        print(sorted(self))
