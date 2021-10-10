# Nico
# 时间：2021/6/1 13:24

# 多线程生产者消费者模式
import queue
import blog_spider
import time
import random
import threading

def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):   # 生产者
    while True:
        url = url_queue.get()           # 获取
        html = blog_spider.craw(url)    # 调用
        html_queue.put(html)            # 输出
        print(threading.currentThread().name, f"craw {url}", "url_queue.size=", url_queue.qsize())
        time.sleep(random.randint(1, 2))    # 随机睡眠1到2秒

def do_parse(html_queue: queue.Queue, fout):        # 消费者
    while True:
        html = html_queue.get()                     # 获取
        results = blog_spider.parse(html)           # 解析
        for result in results:                      # 写入文件
            fout.write(str(result) + "\n")
        print(threading.currentThread().name, f"results.size", len(results),  "url_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))    # 随机睡眠1到2秒

if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:        # 对url_queue进行初始化
        url_queue.put(url)

    for idx in range(3):        # 3个生产者线程
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
        t.start()               # 启动线程

    fout = open("02.data.txt", "w")

    for idx in range(2):        # 2个消费者线程
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse{idx}")
        t.start()               # 启动线程