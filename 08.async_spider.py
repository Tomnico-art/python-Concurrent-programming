# Nico
# 时间：2021/6/20 16:57

import asyncio  # 引入异步IO模块
import aiohttp
import blog_spider
import time

async def async_craw(url):      # 协程函数
    print("craw url: ", url)
    async  with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")

loop = asyncio.get_event_loop()     # 获取超级循环

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))    # 等待tasks完成
end = time.time()
print("use time seconds: ", end - start)