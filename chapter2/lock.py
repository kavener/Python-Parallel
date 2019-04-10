# import threading
# import time
# resoure = 0

# count = 1000000

# resoure_lock = threading.Lock()


# def increment():
#     global resoure
#     for i in range(count):
#         with resoure_lock:
#                 resoure += 1


# def decerment():
#     global resoure
#     for i in range(count):
#         with resoure_lock:
#                 resoure -= 1
        


# increment_thread = threading.Thread(target=increment)
# decerment_thread = threading.Thread(target=decerment)

# increment_thread.start()
# decerment_thread.start()

# increment_thread.join()
# decerment_thread.join()

# print(resoure)

import threading

lock = threading.Lock()
def dosomething(lock):
    lock.acquire()
    # do something
    lock.release()
    
lock.acquire()
dosomething(lock)
lock.release()