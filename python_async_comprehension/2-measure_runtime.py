#!/usr/bin/env python3
"""
Module for measuring the execution time of multiple
async_comprehension coroutines running concurrently.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute four async_comprehension coroutines concurrently
    and return the total elapsed execution time in seconds.

    Returns:
        float: The time taken to complete all coroutines.
    """
    start = time.perf_counter()

    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    end = time.perf_counter()

    return end - start
    
