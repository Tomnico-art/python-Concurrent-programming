# Nico
# 时间：2021/6/16 13:22

import flask
from concurrent.futures import ProcessPoolExecutor
import math
import json


app = flask.Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route("/is_prime/<number>")    # 定义接口
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)   # 调用进程池
    return json.dumps(dict(zip(number_list, results)))  # 用json返回字典

if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()  # 进程池
    app.run()