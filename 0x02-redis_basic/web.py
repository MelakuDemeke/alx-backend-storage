#!/usr/bin/env python3
import requests
from typing import Callable
from functools import wraps
import redis

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """A decorator function to count the number of requests made to a given URL
    and cache the response using Redis.
    """
    def wrapper(url):
        """ Wrapper for decorator """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Retrieve the content of a given URL using the requests library.
    """
    req = requests.get(url)
    return req.text
