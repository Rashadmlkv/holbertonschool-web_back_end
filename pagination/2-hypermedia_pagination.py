#!/usr/bin/env python3
"""This module contains a Server class to paginate
a database of popular baby names"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns limited data started from start index to
        end index  as a list."""
        assert type(page) is int and type(page_size) is int\
            and page > 0 and page_size > 0

        data_range = Server.index_range(page, page_size)
        start = data_range[0]
        end = data_range[1]

        self.dataset()
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns paginated response"""
        data = self.get_page(page, page_size)
        total_pages = int(len(self.__dataset) / page_size)

        response = {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
        return response

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Returns a tuple of size two containing a start index and
        an end index corresponding to the range of indexes to return
        in a list for those particular pagination parameters"""

        start_index: int = (page - 1) * page_size
        end_index: int = page_size * page

        return (start_index, end_index)
