#!/usr/bin/env python3
"""
Basic serialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): Name of the JSON file

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
