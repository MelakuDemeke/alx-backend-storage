#!/usr/bin/env python3
import redis

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
