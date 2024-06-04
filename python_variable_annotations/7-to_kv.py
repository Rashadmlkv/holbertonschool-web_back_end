#!/usr/bin/env python3
"""
    Script Documentation
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Method Documentation
    """
    return (k, v ** 2)
