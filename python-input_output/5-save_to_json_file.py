#!/usr/bin/python3
"""From JSON string to Object"""
import json


def save_to_json_file(my_obj, filename):
    """Define Function"""

    with open(filename, 'w',  encoding='UTF-8') as f:
        json.dump(my_obj, f)
