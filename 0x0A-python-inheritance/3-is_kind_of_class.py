#!/usr/bin/python3
"""Defines an inheritance-checking function"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance or
       inherits from a_class, otherwise false
    """
    return (isinstance(obj, a_class))
