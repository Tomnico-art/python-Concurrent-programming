# Nico
# 时间：2021/6/6 13:35

import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)     # 定义服务
pool = ThreadPoolExecutor()     # 定义全局pool

def read_file():
    time.sleep(0.1)
    return "file result"

def read_db():
    time.sleep(0.2)
    return "db result"

def read_api():
    time.sleep(0.3)
    return "api result"

@app.route("/")
def index():
    result_file = pool.submit(read_file)   # 读取文件
    result_db = pool.submit(read_db)       # 读取数据库
    result_api = pool.submit(read_api)     # 读取api

    return json.dumps({         # 返回json结果
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result()
    })


if __name__ == "__main__":
    app.run()                   # 启动服务