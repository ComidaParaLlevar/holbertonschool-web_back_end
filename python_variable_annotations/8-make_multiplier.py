#!/usr/bin/env python3
"""type-annotated function that takes
a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies float by multiplier"""
    def multiply(n: float):
        """returns product of float and multiplier"""
        return n * multiplier
    return multiply
