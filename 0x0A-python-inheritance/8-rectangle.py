#!/usr/bin/python3
"""Defines a class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle with a
           width and a height.
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
