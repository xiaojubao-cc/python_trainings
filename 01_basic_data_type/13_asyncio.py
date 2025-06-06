#基于的时间循环和协程的单线程，适用于IO密集型任务，感觉类似于redis的多路IO复用
#async await协程对象需要通过 await 关键字或事件循环（event loop）来触发执行。
#网络调用
import asyncio
from dataclasses import dataclass
from typing import Any

import aiohttp

import aiofiles
import aiomysql


#  网络请求多个url返回数据汇总
#fetch函数属于一个协程函数
# async def fetch(session: aiohttp.ClientSession, url:str) -> str:
#     async with session.get(url) as response:
#         return await response.text()
#
# async def main() -> None:
#     urls = ['http://www.baidu.com', 'http://www.hupu.com']
#     async with aiohttp.ClientSession() as session:
#         #这里返回的是协程list
#         tasks = [fetch(session, url) for url in urls]
#         #执行多个协程对象
#         results = await asyncio.gather(*tasks)
#         for result in results:
#             print(result)
#
# asyncio.run(main())
#文件的读写
# async def read_file(filename):
#     async with aiofiles.open(filename, mode='r') as f:
#         content = await f.read()
#         return content
#
# async def main():
#     filenames = ['nba.txt', 'nba.txt']
#     tasks = [read_file(filename) for filename in filenames]
#     results = await asyncio.gather(*tasks)
#     for result in results:
#         print(result)
#
# asyncio.run(main())

#定时周期性任务的执行
# async def task():
#     print('Task is running')
#     await asyncio.sleep(2)  # 模拟耗时任务或等待时间
#     print('Task finished')
#
# async def main():
#     while True:
#         await task()
#         await asyncio.sleep(5)  # 每5秒运行一次任务
#
# asyncio.run(main())

#并发执行多个任务
# async def task1():
#     await asyncio.sleep(2)
#     print('Task 1 done')
#     return 'Result 1'
#
# async def task2():
#     await asyncio.sleep(3)
#     print('Task 2 done')
#     return 'Result 2'
#
# async def main():
#     result1, result2 = await asyncio.gather(task1(), task2())
#     print(f'Results: {result1}, {result2}')
#
# asyncio.run(main())

#执行数据库操作
@dataclass
class User(object):
    id:str
    name:str
    age:int
    info:str

class MysqlOperate(object):
    def __init__(self,host:str,user:str,password:str,db:str):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.pool: aiomysql.Pool = None

    #创建连接池
    async def create_pool(self):
        self.pool = await aiomysql.create_pool(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            loop=asyncio.get_event_loop()
        )

    #查询对象
    async def select_data(self,sql:str) ->list[User]:
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                #组装sql条件
                await cursor.execute(sql)
                data: list = await cursor.fetchall()
        return [User(*u) for u in data]

async def main():
    mo = MysqlOperate('10.1.62.220','root',"root123","eop")
    await mo.create_pool()
    try:
        user_list:list[User] = await mo.select_data("select * from user")
        for user in user_list:
            print(user)
    finally:
        if mo.pool:
            mo.pool.close() #关闭连接池
            await mo.pool.wait_closed() #等待连接池关闭

if __name__ == '__main__':
    asyncio.run(main())