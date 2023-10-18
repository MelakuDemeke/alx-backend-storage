#!/usr/bin/env python3
import redis
from typing import Union
from uuid import uuid4


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
