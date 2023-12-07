#!/usr/bin/env python3
""" More involved type annotations  """
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """ Safely get value

    Func takes a list and returns a list of tuple.

    Args:
    dct (Mapping): A dictionary
    key (Any): Dict key
    default (Union[T, None]): default arg

    Returns:
        T | Any
    """
    if key in dct:
        return dct[key]
    else:
        return default
