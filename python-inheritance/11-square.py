#!/usr/bin/python3
"""Module that defines class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Define Square class"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
