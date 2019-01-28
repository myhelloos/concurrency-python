#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-01-28

import threading

shared_source_with_lock = 0
shared_source_with_no_lock = 0
COUNT = 100_0000
shared_resource_lock = threading.Lock()

# with lock
def increment_with_lock():
    global shared_source_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_source_with_lock += 1
        shared_resource_lock.release()

def decrement_with_lock():
    global shared_source_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_source_with_lock -= 1
        shared_resource_lock.release()

# without lock
def increment_without_lock():
    global shared_source_with_no_lock
    for i in range(COUNT):
        shared_source_with_no_lock += 1

def decrement_without_lock():
    global shared_source_with_no_lock
    for i in range(COUNT):
        shared_source_with_no_lock -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(shared_source_with_lock)
    print(shared_source_with_no_lock)