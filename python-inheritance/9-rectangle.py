#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from BaseGeometry
(task based on 8-rectangle.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle using BaseGeometry validation,
    with area calculation and custom string representation.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the printable string representation of the rectangle.

        Returns:
            str: Description of the rectangle in [Rectangle] <width>/<height>
            format.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
