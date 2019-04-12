import threading
import random
import time

# 假定商品序号
goods = 0

# 定义一个事件
event = threading.Event()

def consumer():

    time.sleep(0.5)
    print(threading.currentThread().getName() + ' consumer is wait for goods.\n')

    # 等待事件，进入阻塞状态
    event.wait()

    print(threading.currentThread().getName() + ' consumer gets the goods: {}\n'.format(goods))

def producer():
    global goods
    time.sleep(1)
    goods = random.randint(1, 11)
    print('producer makes the goods: {}\n'.format(goods))
    time.sleep(1)
    # Flag --> True
    event.set()

if __name__ == "__main__":
    thread_consumer1 = threading.Thread(target=consumer) 
    thread_consumer2 = threading.Thread(target=consumer) 
    thread_producer = threading.Thread(target=producer) 

    thread_consumer1.start()
    thread_consumer2.start()
    thread_producer.start()

    thread_consumer1.join()
    thread_consumer2.join()
    thread_producer.join()

    print('consumer-producer example end.')




