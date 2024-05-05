#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that returns new function"""
    def multiply_with_n(number: float) -> float:
        """function that multiplies number with multiplier"""
        return number * multiplier
    return multiply_with_n
