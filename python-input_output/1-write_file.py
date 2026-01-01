#!/usr/bin/python3
"""Write File"""


def write_file(filename="", text=""):
    "Define Write File"

    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
