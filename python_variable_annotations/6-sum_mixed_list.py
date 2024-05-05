#!/usr/bin/env python3
"""Complex types - mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function that finds sum of mixed list"""
    sum = 0
    for value in mxd_lst:
        sum += value
    return sum
