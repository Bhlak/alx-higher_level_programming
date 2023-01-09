#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square that is a subclass of Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
