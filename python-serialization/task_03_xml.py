#!/usr/bin/env python3
"""
This module provides functionality to serialize a Python dictionary to an XML
file and deserialize an XML file back into a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary containing data to serialize.
        filename (str): The target XML file path.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The source XML file path.

    Returns:
        dict: A Python dictionary reconstructed from the XML data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        reconstructed_dict = {}
        for child in root:
            reconstructed_dict[child.tag] = child.text

        return reconstructed_dict

    except (FileNotFoundError, ET.ParseError, Exception):
        return {}
