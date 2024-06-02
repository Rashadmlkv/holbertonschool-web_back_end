#!/usr/bin/env python3
"""
This module containes regular function
that returns asyncio.Task
"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay
    and returns a asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
