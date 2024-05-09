#!/usr/bin/env python3
"""Duck typing"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns length"""
    return [(i, len(i)) for i in lst]
