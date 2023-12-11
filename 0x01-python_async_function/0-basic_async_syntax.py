#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay

    Args:
    max_delay (int): max delay time

    Returns:
        float: A random float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
