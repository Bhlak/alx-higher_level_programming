#!/usr/bin/python3
"""Defines a subclass to a Class list"""


class MyList(list):
    """Defines a class Mylist with a list superclass"""
    def print_sorted(self):
        print(sorted(self))
