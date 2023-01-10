#!/usr/bin/python3
"""Writes a string to a file"""


def write_file(filename="", text=""):
    """Writes to a text file and returns the number
       of characters written
    """

    total = 0
    with open(filename, 'w', encoding="utf-8") as f:
        total = f.write(text)

    return total
