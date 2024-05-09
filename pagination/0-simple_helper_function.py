#!/usr/bin/env python3
"""Task 0"""


def index_range(page, page_size):
    """returns tuple of start and end indexses"""
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return start_index, end_index
