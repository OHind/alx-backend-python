#!/usr/bin/env python3
""" Documentation """

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ function docs """
    start_time = asyncio.get_running_loop().time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return (asyncio.get_running_loop().time() - start_time)
