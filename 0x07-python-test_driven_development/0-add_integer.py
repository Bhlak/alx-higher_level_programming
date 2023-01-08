#!/usr/bin/python3
"""Defines a function add_integer
    Parameters: a(int)
                b(int)
        Returns: Sum of two values
"""



def add_integer(a, b=98):
    """Adds two integers
        Raises: TypeError: if values are not integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int)and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b

