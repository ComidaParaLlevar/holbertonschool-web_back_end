#!/usr/bin/env python3
"""type-annotated function that takes a list input_list of integers and floats and returns their sum as a float"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns sum of integers and floats in list"""
    return sum(mxd_list)
