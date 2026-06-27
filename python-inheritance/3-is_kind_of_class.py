#!/usr/bin/python3
"""This module provides a function to check if an object is an instance of,
or if the object is an instance of a class that inherited from, a class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of, or inherited from, a_class.

    Returns:
        True if obj is an instance or inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
