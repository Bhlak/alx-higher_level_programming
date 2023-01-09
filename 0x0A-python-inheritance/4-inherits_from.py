#!/usr/bin/python3
"""Defines a function to check for inheritance"""


def inherits_from(obj, a_class):
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
