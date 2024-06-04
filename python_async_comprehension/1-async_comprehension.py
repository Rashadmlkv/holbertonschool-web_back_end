#!/usr/bin/env python3
"""
    Script Documentation
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
        Method Documentation
    """
    return [i async for i in async_generator()]
