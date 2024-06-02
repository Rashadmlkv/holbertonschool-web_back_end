#!/usr/bin/env python3
"""
The module that contains type-annotated function that
takes a float as argument and returns a function that
multiplies a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that takes float as an arg and returns float"""
    def inner(value: float) -> float:
        return value * multiplier

    return inner
