#!/usr/bin/python3
"""
This module provides a function to convert an object to a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns the object from json."""
    return json.loads(my_str)
