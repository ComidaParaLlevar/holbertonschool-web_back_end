#!/usr/bin/env python3
"""type-annotated coroutine that takes in an integer argument"""
import asyncio
import random

def wait_random(max_delay = 10):
    """returns random float number"""
    waiting = random.uniform(0, max_delay)
    await asyncio.sleep(waiting)
    return waiting
