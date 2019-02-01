#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-01

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Staring %s \n" % name)
    time.sleep(3)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(name="background_process", target=foo)
    background_process.daemon = True
    no_background_process = multiprocessing.Process(name="no_background_process", target=foo)
    no_background_process.daemon = False
    background_process.start()
    no_background_process.start()
  