#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-01-28
import threading
from time import sleep


def function(i):
    sleep(.5)
    print("function called by thread %i" % i)
    return

threads = []

for i in range(10):
    t = threading.Thread(target = function, args=(i, ))
    threads.append(t)
    t.start()
