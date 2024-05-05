#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function that measures runtime for 4 times of script"""
    f = async_comprehension
    total_runtime = time()
    total_runtime_list = [f(), f(), f(), f()]
    total_runtime_list = await gather(*total_runtime_list)
    return time() - total_runtime
