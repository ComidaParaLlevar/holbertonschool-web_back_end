#!/usr/bin/env python3
"""return values with correct types"""


def element_length(lst: list[str]) -> list[tuple[str, int]]:
    """returns list of tuples with string and int"""
    return [(i, len(i)) for i in lst]
