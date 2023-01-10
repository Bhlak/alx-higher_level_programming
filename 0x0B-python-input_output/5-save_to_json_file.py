#!/usr/bin/python3
"""Writes object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file
       using JSON representation
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
