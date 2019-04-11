import threading
import random
import time

semaphore = threading.Semaphore(0)

# 假设生产的资源
item_number = 0

# 消费者
def consumer():
    print('Consumer is waiting for Producer')

    # 等待获取信号量
    semaphore.acquire()

    print('get the product , number is {}'.format(item_number))
    time.sleep(3)
# 生产者
def producer():
    global item_number

    # 模拟生产资源过程
    time.sleep(2)
    item_number = random.randint(1, 100)
    time.sleep(2)

    print('made the product , number is {}'.format(item_number))

    # 释放资源
    semaphore.release()

if __name__ == "__main__":
    for i in range(5):

        # 将生产者、消费者实例化为线程
        thread_consumer = threading.Thread(target=consumer)
        thread_producer = threading.Thread(target=producer)

        thread_consumer.start()
        thread_producer.start()

        thread_consumer.join()
        thread_producer.join()

    print('consumer-producer example end.')

# import threading
# import random
# import time

# # 信号量为三即能够释放的资源为三次
# semaphore = threading.Semaphore(3)      # 互斥锁+队列   相当于一个容器，容器里同时最大可以存在五个钥匙，同时也只能有五个线程，
#                                         # 谁先拿到并释放后，下一个才能拿到钥匙

# # 假定url序号
# order = 0

# def spider():
#     global order
#     with semaphore:
#         # 模拟采集过程
#         time.sleep(2)
#         order +=1
        
#         print('{} is crawlering on {}th url'.format(threading.currentThread().getName(), order))
#         time.sleep(2)
         
# Threads = []
# for i in range(10):
#     t = threading.Thread(target=spider)
#     Threads.append(t)
#     t.start()
    
# for t in Threads:
#     t.join()

# print('Spider end.')
