#!/usr/bin/env python3
"""type-annotated coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns random float number"""
    for_wait = random.uniform(0, max_delay)
    await asyncio.sleep(for_wait)
    return for_wait
