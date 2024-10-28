#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        Ensures deletion resilience.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary for deletion-resilient hypermedia pagination.
        """
        indexed_data = self.indexed_dataset()

        # Assert index is valid
        assert isinstance(index, int) and 0 <= index < len(indexed_data), \
            "Index out of range"

        data = []
        current_index = index
        items_count = 0

        # Loop through dataset until the page size is met
        while items_count < page_size and current_index < len(indexed_data):
            item = indexed_data.get(current_index)
            if item:
                data.append(item)
                items_count += 1
            current_index += 1

        # Determine next index or None if out of range
        next_index = current_index if current_index < len(indexed_data) \
            else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': items_count,
            'data': data
        }
