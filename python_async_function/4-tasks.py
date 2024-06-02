#!/usr/bin/env python3
"""
This module contains function that and calls
asyncio task
"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that calls task_wait_random function
    """
    delays = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))

    return sorted(delays)
