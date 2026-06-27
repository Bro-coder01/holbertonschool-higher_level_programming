#!/usr/bin/python3
"""This module defines an abstract class Shape, its subclasses Circle
and Rectangle, and a standalone function shape_info to demonstrate
duck typing in Python.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a geometric shape interface."""

    @abstractmethod
    def area(self):
        """Abstract method to compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a Circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initializes a Circle instance with a given radius."""
        self.radius = radius

    def area(self):
        """Computes and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Computes and returns the perimeter of the circle."""
        returnNormally I can help with things like this, but I don't seem to have access to that content. You can try again or ask me for something else.
