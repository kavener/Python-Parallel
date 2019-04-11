import threading
import time
resoure = 0

count = 1000000

semaphore = threading.Semaphore(1)


def increment():
    global resoure
    for i in range(count):
        semaphore.acquire()
        resoure += 1
        semaphore.release()

def decerment():
    global resoure
    for i in range(count):
        semaphore.acquire()
        resoure -= 1
        semaphore.release()


increment_thread = threading.Thread(target=increment)
decerment_thread = threading.Thread(target=decerment)

increment_thread.start()
decerment_thread.start()

increment_thread.join()
decerment_thread.join()

print(resoure)