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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Retrieves a value from Redis storage.

        Args:
        key (str): The key of the data to retrieve.
        fn (Callable): Callable argument used to convert the data back to the desired format.

        Returns:
        The stored data
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieves a string value from a Redis data storage.
        '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieves an integer value from a Redis data storage.
        '''
        return self.get(key, lambda x: int(x))
