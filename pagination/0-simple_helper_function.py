#!/usr/bin/env python3
"""This module contains a function named index_range that
takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters"""

    start_index: int = (page - 1) * page_size
    end_index: int = page_size * page

    return (start_index, end_index)
