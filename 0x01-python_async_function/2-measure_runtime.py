#!/usr/bin/env python3
""" 2. Measure the runtime """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of a function

    Args:
    n (int): number of times
    max_delay (int): max delay time

    Returns:
        float: A float
    """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
