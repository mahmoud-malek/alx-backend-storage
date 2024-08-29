# 0x02. Redis Basic

## Overview
This project covers the fundamentals of using Redis, a powerful and efficient in-memory data structure store. It provides an introduction to Redis, its key features, and basic usage examples.

## Features
- Overview of Redis
- Installation instructions
- Basic data storage and retrieval examples
- Key commands and functionalities
- References and resources

## Installation
Follow these steps to install and set up Redis:
1. Download and install Redis from [Redis official website](https://redis.io/download)
2. Configure Redis according to your system requirements
3. Start the Redis server
4. Validate the installation by running `redis-cli --version`

## Usage
To use Redis for basic data storage and retrieval, follow these examples:
1. Connect to the Redis server using `redis-cli`
2. Set a key-value pair using the `SET` command
```shell
SET mykey "Hello Redis"
```
3. Retrieve the value using the `GET` command
```shell
GET mykey
```

## Commands
Here are some of the commonly used commands in Redis:
- `SET key value`: Set a key with the specified value
- `GET key`: Retrieve the value associated with the key
- `DEL key`: Delete a key and its value
- `FLUSHALL`: Flush all keys from the current database

## Resources
- [Redis Documentation](https://redis.io/documentation)
- [Redis Commands Reference](https://redis.io/commands)
- [Redis Quick Start](https://redis.io/topics/quickstart)

Feel free to explore more advanced features and functionalities of Redis to enhance your real-world applications.

---
This README.md file is generated with ❤️ by an AI assistant.