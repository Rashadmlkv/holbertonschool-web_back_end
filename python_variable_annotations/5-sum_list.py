#!/usr/bin/env python3
"""
The module that contains type-annotated function sum_list
which takes a list input_list of floats as argument and
returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates sum of the elements of the list"""
    return sum(input_list)
