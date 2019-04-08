from threading import Thread
from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = 'Hello Python Parallel'

    def print_message(self):
        print(self.message)

    def run(self):

        print('Parallel start!\n')
        i = 0
        while i <= 9:
            self.print_message()
            sleep(2)
        
            i += 1
        print('Parallel end!\n')

print('Process Started')

hello_parallel = CookBook()

hello_parallel.start()

print('Process end')

