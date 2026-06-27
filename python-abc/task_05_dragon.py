#!/usr/bin/python3
"""
This module defines mixin classes for swimming and flying behaviors,
and a Dragon class that combines both functionalities using multiple inheritance.
"""


class SwimMixin:
    """Mixin class to add swimming behavior."""

    def swim(self):
        """Prints a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying behavior."""

    def fly(self):
        """Prints a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from both SwimMixin and FlyMixin."""

    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
