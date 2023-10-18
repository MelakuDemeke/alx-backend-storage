#!/usr/bin/env python3
import requests
from typing import Callable
from functools import wraps


def count_req(method: Callable) -> Callable:

    @wraps(method)
    def wrapper(url):
        pass


def get_page(url: str) -> str:
    req = requests.get(url)
    req_text = req.text
    return req_text
