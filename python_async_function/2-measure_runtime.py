#!/usr/bin/env python3
"""
This module contains function that measures execution
time for the another function
"""
import time
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n
    """
    before_execution = time.time()
    asyncio.run(wait_n(n, max_delay))
    after_execution = time.time()
    total_time = after_execution - before_execution
    return total_time / n
