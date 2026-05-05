"""
Utility functions for basic arithmetic operations.
"""


def add(a: int, b: int) -> int:
    """
    Adding funciton
    :param a:
    :param b:
    :return:
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtracting funciton
    :param a:
    :param b:
    :return:
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiplying funciton
    :param a:
    :param b:
    :return:
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divide funciton
    :param a:
    :param b:
    :return:
    """
    return a / b

def convert(a: int) -> str:
    """
    Converts to binary representation (0–100, natural numbers only)
    """
    if not isinstance(a, int):
        raise TypeError("not an integer")

    if a < 0:
        raise ValueError("negative number")

    if a > 100:
        raise ValueError("too large")

    return bin(a)[2:]
