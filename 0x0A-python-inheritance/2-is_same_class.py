#!/usr/bin/python3
"""Defines a comparison function for objects and classes"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the
       given class
    """
    return (type(obj) == a_class)
