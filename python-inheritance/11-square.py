#!/usr/bin/python3
"""This module defines a class Square that inherits from Rectangle
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square that inherits from Rectangle
    and includes a custom string representation.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the printable string representation of the square.

        Returns:
            str: Description of the square in [Square] <width>/<height> format.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
