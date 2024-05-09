#!/usr/bin/env python3
"""The basics of async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays """
    tasks = [wait_random(max_delay) for sec in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
