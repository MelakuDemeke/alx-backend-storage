#!/usr/bin/env python3
import requests
from typing import Callable
from functools import wraps
import redis

redis_ = redis.Redis()


def count_req(method: Callable) -> Callable:
    """A decorator function to count the number of requests made to a given URL
    and cache the response using Redis.
    """

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function that decorates the input method.

        Args:
            url (str): The URL to fetch content from.

        Returns:
            str: The content of the URL as a string.
        """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_req
def get_page(url: str) -> str:
    """
    Retrieve the content of a given URL using the requests library.
    """
    return requests.get(url).text
