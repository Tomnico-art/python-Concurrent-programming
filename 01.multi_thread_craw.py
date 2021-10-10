# Nico
# 时间：2021/5/30 22:34

import blog_spider
import threading
import time

# 单线程
def single_thread():
    print("single_thread begin")
    for url  in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")

# 多线程
def multi_thread():
    print("multi_thread begin")
    threads = []                        # 创建thread对象
    for url in blog_spider.urls:        # 给threads这个list添加对象
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )

    for thread in threads:      # 启动多线程
        thread.start()

    for thread in threads:      # 结束多线程
        thread.join()
    print("multi_thread end")

if __name__ == "__main__":
    start = time.time()         # 开始时间
    single_thread()
    end = time.time()           # 结束时间
    print("single thread cost:", end-start, "seconds")

    start = time.time()         # 开始时间
    multi_thread()
    end = time.time()           # 结束时间
    print("multi thread cost:", end-start, "seconds")