#!/usr/bin/env python3
"""Async Generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Couroutine looping 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
