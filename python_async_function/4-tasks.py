#!/usr/bin/env python3
"""Tasks"""


from typing import List
from asyncio import gather
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """running wait_random for n times"""
    wait_list = []
    for i in range(n):
        wait_list.append(task_wait_random(max_delay))
    wait_list = await gather(*wait_list)
    return sorted(wait_list)
