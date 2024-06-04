#!/usr/bin/env python3
"""
    Script Documentation
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Method Documentation
    """
    return [(i, len(i)) for i in lst]
