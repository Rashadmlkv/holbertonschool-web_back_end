#!/usr/bin/env python3
"""Task 2"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """getting page"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index < len(self.dataset()):
            return self.__dataset[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returning formatted dictionary"""
        page_get = self.get_page(page, page_size)
        data = len(self.dataset())
        pages = math.ceil(data / page_size)

        return {
            'page_size': len(page_get),
            'page': page,
            'data': page_get,
            'next_page': page + 1 if page < pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': pages
        }
