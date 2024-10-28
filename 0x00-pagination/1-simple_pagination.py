#!/usr/bin/env python3
"""
This file contains a function named index_range that takes two integer
arguments page and page_size.
"""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on the page number and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_indx, end_indx = index_range(page, page_size)

        dataset = self.dataset()

        if start_indx > len(dataset):
            return []

        return dataset[start_indx:end_indx]
