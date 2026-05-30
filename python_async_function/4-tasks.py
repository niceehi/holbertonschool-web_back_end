#!/usr/bin/env python3
"""
This module provides an asynchronous function that creates
multiple tasks running random delays concurrently and returns
their results in the order they complete.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Executes multiple wait_random tasks concurrently.

    The function creates n asyncio tasks using task_wait_random,
    each of which waits for a random amount of time between
    0 and max_delay seconds. The delay values are collected
    and returned in the order the tasks finish execution.

    Args:
        n (int): The number of tasks to create and run.
        max_delay (int, optional): The maximum possible delay
            for each task in seconds. Defaults to 10.

    Returns:
        List[float]: A list of delay values ordered by task
            completion time.
    """
    tasks = []
    for item in range(n):
        tasks.append(task_wait_random(max_delay))

    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
