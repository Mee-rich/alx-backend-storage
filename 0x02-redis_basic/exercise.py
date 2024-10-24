#!/usr/bin/env python3
""" Task 1: writing strings to Redis
"""

import redis
from uuid import uuid4
from typing import Union

class Cache:
    def __init__(self):
        """ Initialize the Redis client and flush the database. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ This stores the data in Redis and return the randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in Redis.

        Returns:
            str: The key under which data is stored.
        """

        random_key = str(uuid4())

        self._redis.set(random_key, data)

        return random_key
