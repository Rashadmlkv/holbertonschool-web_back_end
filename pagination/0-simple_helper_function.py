#!/usr/bin/env python3
"""
    Script Documentation
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Method Documentation
    """
    return ((page - 1) * page_size, page * page_size)
