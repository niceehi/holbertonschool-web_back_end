#!/usr/bin/env python3
"""
Module containing the async_comprehension coroutine.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect all values produced by async_generator using
    an asynchronous comprehension.

    Returns:
        List[float]: A list of floating-point numbers generated
        by async_generator.
    """
    results = [item async for item in async_generator()]
    return results
