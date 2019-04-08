# import threading
# import time


# # 用于实例化线程目标函数
# def function(i):
#     time.sleep(2)
#     print('Thread {} is running.'.format(i))
#     time.sleep(2)
#     return


# for i in range(1, 6):
#     # Python模块threading.Thread方法
#     t = threading.Thread(target=function, args=(i, ))
#     t.start()
#     # t.join()

import threading
import time


class myThread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i

    def run(self):
        time.sleep(2)
        print('Thread {} is running.'.format(self.i))
        time.sleep(2)
        return


print('Mian THread starting')

threads = []
for i in range(1, 6):
    t = myThread(i)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
print('Mian THread end')
