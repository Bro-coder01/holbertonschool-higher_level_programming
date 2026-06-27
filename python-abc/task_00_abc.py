#!/usr/bin/python3
"""This module defines an abstract base class Animal and its subclasses
Dog and Cat using the abc module.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal structure."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses to return
        the sound of the animal.
        """
        pass


class Dog(Animal):
    """Subclass representing a Dog that inherits from Animal."""

    def sound(self):
        """Returns the specific sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a Cat that inherits from Animal."""

    def sound(self):
        """Returns the specific sound a cat makes."""
        return "Meow"
