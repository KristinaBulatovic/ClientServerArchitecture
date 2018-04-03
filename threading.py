import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

    def run(self, threadLock=None):
        print("Starting " + self.name)
        threadLock.acquire()
        self.print_time(self.name, self.delay, 3)
        threadLock.release()

    threadLock = threading.Lock()
    threads = []
    # Create new threads
    thread1 = threading.myThread(1, "Thread-1", 1)
    thread2 = threading.myThread(2, "Thread-2", 2)
    # Start new Threads
    thread1.start()
    thread2.start()
    # Add threads to thread list

    threads.append(thread1)
    threads.append(thread2)
    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")