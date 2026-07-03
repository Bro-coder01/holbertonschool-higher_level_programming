#!/usr/bin/python3
"""
This module provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file and returns chars."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
