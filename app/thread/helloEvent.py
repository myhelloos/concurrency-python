#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-01-28

import time
from threading import Thread, Event
import random

items = []
event = Event()


class consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print("consumer notify : %d poped from list by %s" % (item, self.name))


class producer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for i in range(100):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item)
            print("producer notify : item %d appended to list by %s" % (item, self.name))
            print("producer notify : event by %s" % self.name)
            self.event.set()
            print("producer notify : event cleared by %s" % self.name)
            self.event.clear()

if __name__ == '__main__':
    producer = producer(items, event)
    consumer = consumer(items, event)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
