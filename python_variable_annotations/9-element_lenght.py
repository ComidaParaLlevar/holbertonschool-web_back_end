#!/usr/bin/env python3
"""return values with correct types"""
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples with string and int"""
    return [(i, len(i)) for i in lst]
