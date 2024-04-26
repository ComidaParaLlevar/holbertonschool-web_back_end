#!/usr/bin/env python3
"""Function that measures the runtime of wait_n"""
import asyncio
import random
from typing import List
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """function that measures the runtime of wait_n"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()
    return (end - start) / n
