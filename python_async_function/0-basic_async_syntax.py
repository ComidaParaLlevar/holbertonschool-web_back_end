#!/usr/bin/env python3
"""type-annotated coroutine that takes in an integer argument"""
import asyncio
import random

def wait_random(max_delay: int = 10) -> float:
    """returns random float number"""
    return random.uniform(0, max_delay)
