import threading
import time

a = 0

def counter():
    time.sleep(1)
    lock.acquire()
    global a
    c = a
    time.sleep(1)
    c = c + 100
    a = c
    print a
    lock.release()

lock = threading.Lock()

for i in range(5):
    t = threading.Thread(target=counter)
    t.start()

