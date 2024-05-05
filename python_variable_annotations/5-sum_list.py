#!/usr/bin/env python3
"""Complex types - list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all elements of float list"""
    sum = 0
    for value in input_list:
        sum += value
    return sum
