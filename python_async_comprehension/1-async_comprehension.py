#!/usr/bin/env python3
"""Async Comprehensions"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function that collect 10 random numbers
    using an async comprehensing over async_generator"""
    async_list = [i async for i in async_generator()]
    return async_list
