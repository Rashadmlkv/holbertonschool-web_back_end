#!/usr/bin/env python3
"""This module contains async function that measures run time"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension 4 times in parallel"""
    before = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    after = time.time()
    return after - before
