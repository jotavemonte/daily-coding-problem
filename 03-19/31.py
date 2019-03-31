'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import asyncio


async def scheduler(f, n, *args):
    await asyncio.sleep(n)
    for arg in args: f(arg)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    commands = asyncio.gather(
        scheduler(print, 5, '5 seconds'),
        scheduler(print, 3, '3 seconds'),
    )
    loop.run_until_complete(commands)
    loop.close
