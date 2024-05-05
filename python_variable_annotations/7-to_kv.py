#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that creates tuple from arguments"""
    new_tuple: Tuple[str, float] = (k, v ** 2)
    return new_tuple
