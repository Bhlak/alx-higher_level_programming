#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    """Defines a class BaseGeometry"""

    def area(self):
        """Does not yet give a value as there is no area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value type and range"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
