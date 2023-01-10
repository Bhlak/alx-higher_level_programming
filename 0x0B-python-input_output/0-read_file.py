#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
