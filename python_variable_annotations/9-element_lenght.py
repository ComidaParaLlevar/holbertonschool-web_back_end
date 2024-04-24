#!/usr/bin/env python3
"""return values with correct types"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """returns list of tuples with string and int"""
    return [(i, len(i)) for i in lst]
