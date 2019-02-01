#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-01

import multiprocessing
import time


def foo():
    print("Starting function")
    time.sleep(0.1)
    print("Finish function")


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print("Process before execution: ", p, p.is_alive())
    p.start()
    print("Process running: ", p, p.is_alive())
    p.terminate()
    print("Process terminated: ", p, p.is_alive())
    p.join()
    print("Process joined: ", p, p.is_alive())
    print("Process exit code: ", p.exitcode)
