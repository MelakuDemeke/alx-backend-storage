#!/usr/bin/env python3
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wraps(self, *args, **kwargs):
        pass

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
    
    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
            val = self._redis.get(key)
            if fn:
                val = fn(val)
            return val

    def get_str(self, key: str) -> str:
        val = self._redis.get(key)
        utf_val = val.decode('utf-8')
        return utf_val

    def get_int(self, key: str) -> int:
        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except Exception:
            val = 0
        return val
