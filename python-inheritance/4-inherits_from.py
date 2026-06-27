#!/usr/bin/python3
"""This module provides a function to check if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited from a_class.

    Returns:
        True if obj is a subclass of a_class (but not a_class itself),
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
