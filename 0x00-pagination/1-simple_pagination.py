#!/usr/bin/env python3
"""Simple pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """The function returns a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    data = page_size * page
    start_index = data - page_size
    end_index = data
    return (start_index, end_index)


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
        assert (page > 0) and (page_size > 0)
        start, end = index_range(page, page_size)
        try:
            self.dataset()
            return self.__dataset[start:end]
        except IndexError:
            return []
