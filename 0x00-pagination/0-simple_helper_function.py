#!/usr/bin/env python3
"""
This file contains a function named index_range that takes two integer
arguments page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    page: The page to fetch from
    page_size: size of contents in the page

    Returns:
        tuple: A tuple (start_index, end_index) representing the range of
               indexes to return for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
