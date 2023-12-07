#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Any, Union, Sequence


# The types of the elements of the input are not know so it a Sequence
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Func takes a unknown input type
    and returns a first el or None.

    Args:
    lst (Sequence): Unknown type - Sequence

    Returns:
        Sequence: first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None
