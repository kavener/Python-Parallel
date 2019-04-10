

import threading
import random
import time

semaphore = threading.Semaphore(0)

# 假设生产的资源
item_number = 0

# 消费者
def consumer():
    print('Consumer is waiting for Producer')

    semaphore.acquire()

    print('get the product , number is '.format(item_number))

# 生产者
def producer():
    global item_number

    # 模拟生产资源过程
    time.sleep(2)
    item_number = random.randint(1, 100)
    time.sleep(2)

    print('made the product , number is '.format(item_number))

    semaphore.release()


for i in range(5):

    # 将生产者、消费者实例化为线程
    thread_consumer = threading.Thread(target=consumer)
    thread_producer = threading.Thread(target=producer)

    thread_consumer.start()
    thread_producer.start()

    thread_consumer.join()
    thread_producer.join()

print(3333, item_number)
print('consumer-producer example end.')
