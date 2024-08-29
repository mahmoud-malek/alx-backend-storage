#!/usr/bin/env python3
"""
Defines a function `get_page`
"""
import redis
import requests
from datetime import timedelta


@cache
def get_page(url: str) -> str:
    """ Uses the requests module to obtain the HTML content of a web page """
    redis = redis.Redis()
    redis.set(f"count:{url}", requests.get(url).text)
    redis.expire(f"count:{url}", timedelta(seconds=10))
    return redis.get(f"count:{url}").decode('utf-8')
