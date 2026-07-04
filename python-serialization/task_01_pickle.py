#!/usr/bin/env python3
"""
This module defines a CustomObject class that can serialize itself to a file
and deserialize from a file using the pickle module.
"""
import pickle


class CustomObject:
    """A custom class representing an object with personal details."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject instance with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance and saves it to a binary file.

        Args:
            filename (str): The destination file path.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and deserializes an instance of CustomObject from a binary file.

        Args:
            filename (str): The source file path.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
