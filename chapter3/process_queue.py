import multiprocessing
import random
import time
from multiprocessing import Queue

# 定义一个进程的队列
def producer(q):
    while True:
        time.sleep(2)
        # 假定商品序号
        item = random.randint(1, 10)
        print('process producer product goods:{}'.format(item))
        q.put(item)
        time.sleep(2)

def consumer(q):
    while True:
        # 即队列中仍然有商品就继续消费，否则等待
        if not q.empty():
            # 消费商品：
            item = q.get()
            print('process cusumer get goods:{}'.format(item))
            time.sleep(1)
        else:
            print('wait for goods...')
            time.sleep(1)
 

if __name__ == "__main__":
    q = Queue()

    process_producer = multiprocessing.Process(target=producer, args=(q,))
    process_consumer = multiprocessing.Process(target=consumer, args=(q, ))

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()





