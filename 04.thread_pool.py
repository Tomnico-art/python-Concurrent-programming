# Nico
# 时间：2021/6/5 15:30

# 线程池ThreadpoolExcutor的使用
import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)    # pool.map方式
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)       # pool.submit方式
        futures[future] = url

    #for future, url in futures.items():
    #    print((url, future.result()))

    for future in concurrent.futures.as_completed(futures):     # 传入的是key
        url = futures[future]
        print(url, future.result())


