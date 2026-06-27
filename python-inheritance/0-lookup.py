#!/usr/bin/python3
"""Module that contains a function for looking up object attributes."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
