#!/usr/bin/env python3
"""Module that contains function - asynchronous
coroutine that waits for a random delay between 0
and max_delay seconds and returns it."""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that waits for
    a random delay between 0 and max_delay
    seconds and returns it.
    """
    delay_time = uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
