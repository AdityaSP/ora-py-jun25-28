import time
import threading

def heavyduty():
    print "Started"
    time.sleep(5)
    print "Ended"

s = time.time()
# heavyduty()
# heavyduty()
# heavyduty()
# heavyduty()
# heavyduty()

t1 = threading.Thread(target=heavyduty)
t2 = threading.Thread(target=heavyduty)
t3 = threading.Thread(target=heavyduty)
t4 = threading.Thread(target=heavyduty)
t5 = threading.Thread(target=heavyduty)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t5.join()
e = time.time()
print "Took: ", e-s