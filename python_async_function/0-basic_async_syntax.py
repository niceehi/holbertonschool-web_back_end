#!/usr/bin/env python3
"""
This module defines an asynchronous function that pauses execution
for a random period of time and returns the delay duration.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Suspends execution for a randomly generated delay between
    0 and the specified maximum value.

    Args:
        max_delay (int, optional): The upper limit for the random
            delay in seconds. Defaults to 10.

    Returns:
        float: The randomly selected delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
