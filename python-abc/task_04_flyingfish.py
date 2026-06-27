#!/usr/bin/python3
"""This module explores multiple inheritance in Python by defining
the Fish and Bird parent classes, and a FlyingFish subclass that
overrides their methods.
"""


class Fish:
    """Class representing a Fish with swim and habitat attributes."""

    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the natural habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird with fly and habitat attributes."""

    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the natural habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a FlyingFish that inherits from both Fish and Bird

    demonstrating multiple inheritance and method resolution order.
    """

    def fly(self):
        """Overrides the fly method to specify flying fish behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method to specify flying fish behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method to describe its combined environment."""
        print("The flying fish lives both in water and the sky!")
