#usr/bin/python3

"""
This module provides an asynchronous function that runs
multiple random delays concurrently and returns their
results in the order they complete.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Executes the wait_random coroutine n times concurrently
    """
    tasks = []
    for item in range(n):
        tasks.append(wait_random(max_delay))

    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
