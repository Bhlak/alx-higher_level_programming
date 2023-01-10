#!/usr/bin/python3
"""Returns an object from JSON"""
import json


def from_json_string(my_str):
    """Converts JSON string to python object"""
    return json.loads(my_str)
