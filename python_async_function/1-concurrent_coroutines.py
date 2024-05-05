#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""


from typing import List
from asyncio import gather
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """running wait_random for n times"""
    wait_list = []
    for i in range(n):
        wait_list.append(wait_random(max_delay))
    wait_list = await gather(*wait_list)
    return sorted(wait_list)
