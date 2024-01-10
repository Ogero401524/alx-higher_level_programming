#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to read.

    Returns:
    - object: The Python object created from the JSON file.

    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
