import threading
import time

a = 0
def producer():
    print "Producer: Started"
    time.sleep(10)
    global a
    a = 100
    print "Producer: Set the value"
    e.set()

def consumer():
    print "Consumer: Started"
    time.sleep(5)
    e.wait()
    # dirty read without the event. e.wait forces the thread to wait till e.set
    print "Consumer: Accessing a", a

# initially in unset state
e = threading.Event()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()