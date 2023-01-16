#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""


class Square:
    """
    class Square definition
    Args:
        size : size of a side in square
    """
    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            size: size of a side of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
