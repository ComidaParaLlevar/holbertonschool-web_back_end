#!/usr/bin/env python3
"""type-annotated function that takes
a float multiplier as argument"""

def make_multiplier(multiplier: float):
    """returns function that multiplies float by multiplier"""
    def multiply(n: float) -> float:
        """returns product of float and multiplier"""
        return n * multiplier
    return multiply
