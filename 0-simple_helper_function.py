#!/usr/bin/env python3
""" Write a function named `index_range` that
    takes two integers args `page` and `page_size`
    and returns a tuplee containing the start index
    and the end corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int):
    """
    returns a tuple (start index, end index)
    """
    return ((page - 1) * page_size, page_size * page)
