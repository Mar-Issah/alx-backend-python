#!/usr/bin/env python3

""" 2. Run time for four parallel comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Runs four times in parallel using asyncio.gather

    Args:
    None

    Returns:
        float: Total runtime measured
    """
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
