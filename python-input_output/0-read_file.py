#!/usr/bin/python3\
"""Read File"""


def read_file(filename=""):
    """Define Read File"""

    with open(filename, encoding="utf-8") as f:

        print(f.read(), end="")
