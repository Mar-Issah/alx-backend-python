#!/usr/bin/env python3
""" 4. Tasks"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time

    Args:
    n (int): number of execution
    max_delay (int): max delay time

    Returns:
        float: List of random float.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
