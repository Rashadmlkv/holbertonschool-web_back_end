#!/usr/bin/env python3
"""
    Script Documentation
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Method Documentation
    """
    def multiply(num: float) -> float:
        """
            Method Documentation
        """
        return num * multiplier
    return multiply
