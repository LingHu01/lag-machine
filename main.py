import asyncio
import multiprocessing
import random

async def async_task(task_name):
    i = 0
    for x in range(10**100000000):
        i += 1
        print(i)

def run_async_task(task_name):
    asyncio.run(async_task(task_name))

if __name__ == '__main__':
    if random.choice([True, False]):
        tasks = ['Task ' + str(i) for i in range(10**100)]

        with multiprocessing.Pool(processes=len(tasks)) as pool:
            pool.map(run_async_task, tasks)

    else:
        pass
