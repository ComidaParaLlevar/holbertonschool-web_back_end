#!/usr/bin/env python3
"""type-annotated function that takes a string
k and an int OR float v as arguments"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple(str, float):
    """returns tuple of string and float"""
    return (k, v * v)
