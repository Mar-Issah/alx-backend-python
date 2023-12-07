#!/usr/bin/env python3
""" Let's duck type an iterable object"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Func takes a list and returns a list of tuple.

    Args:
    lst (Iterable[Sequence]): Iterable Sequence

    Returns:
        List: a list of tuple
    """
    return [(i, len(i)) for i in lst]
