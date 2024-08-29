#!/usr/bin/env python3
"""
Defines a function `get_page` with caching and counting
"""
import redis
import requests
from functools import wraps

# Connect to Redis
redis_client = redis.Redis()


def cache_page(func):
    @wraps(func)
    def wrapper(url: str) -> str:
        # Check if the URL is cached
        cached_content = redis_client.get(f"content:{url}")
        if cached_content:
            # Increment the access count
            redis_client.incr(f"count:{url}")
            return cached_content.decode('utf-8')

        # If not cached, fetch the content
        content = func(url)

        # Cache the content with an expiration time of 10 seconds
        redis_client.setex(f"content:{url}", 10, content)

        # Initialize the access count
        redis_client.set(f"count:{url}", 1)

        return content
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """ Uses the requests module to obtain the HTML content of a web page """
    response = requests.get(url)
    return response.text
