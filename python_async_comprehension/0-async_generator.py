#!/usr/bin/env python3
"""
Module containing an asynchronous generator that produces
random floating-point numbers.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yield 10 random floating-point numbers between 0 and 10.

    The generator pauses for one second before producing
    each value.

    Yields:
        float: A random number in the range [0, 10].
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
