# Nico
# 时间：2021/6/2 13:21

# 线程安全问题及其解决方案
import threading
import time

lock = threading.Lock()

class Account:
    def __init__(self, balance):
        self.balance = balance

def draw(account, amount):
    with lock:      # 用lock解决线程安全问题
        if account.balance >= amount:
            time.sleep(0.1)     # 阻塞线程，使线程切换
            print(threading.currentThread().name, "取钱成功")
            account.balance -= amount
            print(threading.currentThread().name, "余额", account.balance)
        else:
            print(threading.currentThread().name, "取钱失败，余额不足")

if __name__ == "__main__":
    account = Account(1000)     # 初始化，账户1000
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))  # 线程ta
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))  # 线程tb

    ta.start()
    tb.start()