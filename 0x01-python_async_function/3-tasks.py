#!/usr/bin/env python3
""" 3. Tasks """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Wait for a task

    Args:
    max_delay (int): max delay time

    Returns:
        float: Task
    """
    task = create_task(wait_random(max_delay))
    return task
