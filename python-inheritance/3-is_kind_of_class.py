#!/usr/bin/python3
"""Defines a function that checks object class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is instance of a_class or its subclass."""
    return isinstance(obj, a_class)
