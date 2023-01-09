#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """Defines a subclass of int"""
    def __eq__(self, value):
        """== now !="""
        return int(self) != value

    def __ne__(self, value):
        """!= now =="""
        return int(self) == value
