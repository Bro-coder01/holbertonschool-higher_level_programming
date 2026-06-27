#!/usr/bin/python3
"""This module defines a base class BaseGeometry with a public instance
method intended for geometry operations.
"""


class BaseGeometry:
    """A base class representing geometry structures and containing methods
    to be overridden by subclasses.
    """

    def area(self):
        """Raises an Exception indicating that the method is not implemented

        Raises:
            Exception: always raised with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
