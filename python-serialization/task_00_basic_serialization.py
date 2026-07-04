#!/usr/bin/env python3
"""
This module provides basic serialization and deserialization functionalities
for Python dictionaries using the JSON format.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a specified JSON file.

    Args:
        data (dict): A Python dictionary containing the data to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Loads and deserializes data from a specified JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
