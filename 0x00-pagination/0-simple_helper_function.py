#!/usr/bin/env python3
"""
Defines a function named index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes
    """
    nextPageIndex = page * page_size
    return nextPageIndex - page_size, nextPageIndex
