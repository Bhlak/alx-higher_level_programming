#!/usr/bin/python3
"""Returns dictionary description of an object"""


def class_to_json(obj):
    """Returns dictionary desccription of simple data structure"""
    return obj.__dict__
