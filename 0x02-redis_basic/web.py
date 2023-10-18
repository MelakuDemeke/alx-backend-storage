#!/usr/bin/env python3
import requests
from typing import Callable
from functools import wraps
import redis


def count_req(method: Callable) -> Callable:
    redis = redis.Redis()

    @wraps(method)
    def wrapper(url):
        redis.incr(f"count:{url}")
        cached_html = redis.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


def get_page(url: str) -> str:
    req = requests.get(url)
    req_text = req.text
    return req_text
