#!/usr/bin/env python3
import redis
from typing import Union

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, float, int]) -> str:
        pass
