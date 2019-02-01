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
    process_with_name = multiprocessing.Process(name="foo_process", target=foo)
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()