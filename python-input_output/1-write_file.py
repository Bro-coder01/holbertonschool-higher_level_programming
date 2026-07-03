#!/usr/bin/python3
"""
This module provides a function to write text to a file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number of chars."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
