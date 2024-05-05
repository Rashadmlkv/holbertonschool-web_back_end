#!/usr/bin/env python3
"""The basics of async"""


import asyncio
from random import uniform
import time


async def wait_random(max_delay: int = 10) -> float:
    """function that make sleep for random seconds"""
    sleep = uniform(0, max_delay)
    await asyncio.sleep(sleep)
    return sleep
