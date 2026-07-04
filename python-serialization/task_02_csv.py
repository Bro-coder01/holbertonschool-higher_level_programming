#!/usr/bin/env python3
"""
This module provides a function to convert CSV data into JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts data from a CSV file into JSON format and saves it to data.json.

    Args:
        csv_filename (str): The filename of the source CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, Exception):
        return False
