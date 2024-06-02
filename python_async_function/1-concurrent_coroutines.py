#!/usr/bin/env python3
"""
This module contains an async routine called wait_n
that imports wait_random from another Python file.
It takes in two integer arguments (n and max_delay)
and spawns wait_random n times with the specified max_delay.
wait_n returns a list of all the delays (float values) in
ascending order without using sort() due to concurrency considerations.
"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with
    the specified max_delay and returns a list of delays in
    ascending order.
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
