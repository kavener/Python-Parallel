import threading

resoure_lock = 0

count = 1000

resoure_lock_lock = threading.Lock()

def increment():
    global resoure_lock
    for i in range(count):
        resoure_lock += 1
        # print(res)

def decerment():
    global resoure_lock
    for i in range(count):
        resoure_lock -= 1

increment_thread = threading.Thread(target=increment)
decerment_thread = threading.Thread(target=decerment)

increment_thread.start()
decerment_thread.start()

increment_thread.join()
decerment_thread.join()

print(resoure_lock)