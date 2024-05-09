#!/usr/bin/env python3
"""The basics of async"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays """
    tasks = [task_wait_random(max_delay) for sec in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
