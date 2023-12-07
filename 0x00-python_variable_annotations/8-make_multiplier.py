#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    Args:
        multiplier(float): the multiplier

    Returns:
        f: a function

    """
    def f(n: float) -> float:
        """ multiplies a float by the multiplier """
        return float(n * multiplier)

    return f
