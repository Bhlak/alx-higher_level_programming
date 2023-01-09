#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """Defines a class BaseGeometry"""

    def area(self):
        """Does not yet give a value as there is no area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value type and range"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
