#!/usr/bin/python3
"""Defines a function to add attributes to objects"""


def add_attribute(obj, att, value):
    """Add new attribute to obj if possible"""
    if not hasattr(obj, __dict__):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
