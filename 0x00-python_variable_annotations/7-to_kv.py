#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Func takes a string, an int OR float as args
    returns a tuple.
    Args:
    k (str): the string
    v ( Union[int, float]): the list of int and float

    Returns:
        tuple: tuple of the args
    """
    return (k, v**2)
