import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    balls = 0
    speed = 7
    for ball in range(5):
        await asyncio.sleep(speed - power)
        balls += 1
        print(f'Силач {name} поднял {balls} шар')
    print(f'Силач {name} закончил соревнования.')

async def start():
    man1 = asyncio.create_task(start_strongman('Dart Vader', 5))
    man2 = asyncio.create_task(start_strongman('Chipollino', 3))
    man3 = asyncio.create_task(start_strongman('SpiderMan', 4))
    await man1
    await man2
    await man3
    print('Конец соревнования')

asyncio.run(start())



