import threading
import queue
import random
import time

# 创建一个队列
q = queue.Queue()

# 假定商品序号
item = 0


def produecr():
    global item
    while True:
        time.sleep(1)
        item = random.randint(1, 10)
        # 将一个“商品”推到队列中
        q.put(item)
        print('producer {}th gooos append to q.'.format(item))
        time.sleep(1)


def consumer():
    while True:
        # 在队列中删除一个“商品”，并返回该“商品”
        item = q.get()
        print(threading.currentThread().getName() +
              'consumer get {}th goods from q.'.format(item))
        q.task_done()


if __name__ == "__main__":
    threads_consumr = []
    for i in range(3):
        t = threading.Thread(target=consumer)
        t.start()
        threads_consumr .append(t)

    thread_producer = threading.Thread(target=produecr)
    thread_producer.start()
    q.join()
    for t in threads_consumr:
        t.join()
    thread_producer.join()
