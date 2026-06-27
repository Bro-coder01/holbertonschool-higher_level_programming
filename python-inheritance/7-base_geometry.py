#!/usr/bin/python3
"""This module defines a base class BaseGeometry with public instance
methods for area calculation and integer validation.
"""


class BaseGeometry:
    """A base class representing geometry structures and containing validation
    and calculation utilities for geometrical objects.
    """

    def area(self):
        """Raises an Exception indicating that the method is not implemented

        Raises:
            Exception: always raised with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a given value is a strictly positive integer.

        Args:
            name (str): The name associated with the value being validated.
            value (int): The value to be checked.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
