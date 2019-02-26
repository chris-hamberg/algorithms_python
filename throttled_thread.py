from threading import Thread
from datetime import datetime
import time, random

class ThrottledThread(Thread):

    def __init__(self):
        super().__init__()
        self.last_accessed = datetime.now()
        self.data = 0

    def run(self):
        for i in range(10):
            self.sleep()
            if self.sleep_seconds > 0:
                print('{} sleeping for {} seconds'.format(
                    self.getName(), self.sleep_seconds))
                time.sleep(self.sleep_seconds)
            self.last_accessed = datetime.now()
            self.data = random.randint(1, 10)
            print('{} Data: {}'.format(
                self.getName(), self.data))

    def sleep(self):
        self.delay = random.randint(1, 10)
        self.sleep_seconds = self.delay - (
                datetime.now() - self.last_accessed
                ).seconds

threads = [ThrottledThread() for thread in range(10)]
