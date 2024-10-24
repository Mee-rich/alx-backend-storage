#!/usr/bin/env python3

import requests
import redis
from functools import wraps
from typing import Callable, Optional

# Initialize Redis client
redis_store = redis.Redis()

def cache_page(expiration: int = 10):
    """
    Decorator to cache the output of a fetched page for a certain period.

    Args:
        expiration (int): Expiration time for the cached result in seconds.
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def invoker(url: str) -> str:
            """
            Wrapper function that caches the output of the URL fetching method.
            """
            # Generate Redis keys for count and result
            count_key = f'count:{url}'
            result_key = f'result:{url}'

            # Increment the access count for this URL
            redis_store.incr(count_key)

            # Check if the result is already cached
            cached_result = redis_store.get(result_key)
            if cached_result:
                print(f"Cache hit for {url}")
                return cached_result.decode('utf-8')

            # Cache miss: Fetch the page content
            print(f"Cache miss for {url}. Fetching content...")
            try:
                result = method(url)
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                return f"Failed to retrieve {url}: {e}"

            # Cache the result with expiration time
            redis_store.setex(result_key, expiration, result)
            return result

        return invoker
    return decorator


@cache_page(expiration=10)
def get_page(url: str) -> str:
    """
    Fetches the content of a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)
    return response.text


# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/"

    # First call - cache miss, fetches from the URL
    print(get_page(url))

    # Second call - within 10 seconds, should be a cache hit
    print(get_page(url))

    # Check how many times the URL has been accessed
    access_count = redis_store.get(f'count:{url}')
    print(f"URL {url} accessed {int(access_count)} times.")

