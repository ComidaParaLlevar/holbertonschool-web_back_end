#!/usr/bin/env python3
"""type-annotated function that takes a list input_list
of floats as argument and returns their sum as a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of floats in list"""
    return sum(input_list)
