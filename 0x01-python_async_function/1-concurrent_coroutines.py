#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time

    Args:
    n (int): number of execution
    max_delay (int): max delay time

    Returns:
        float: List of random float
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
