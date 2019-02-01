#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-01

import multiprocessing
import time

def foo(i):
    time.sleep(1)
    print("called function in process %s" % i)
    return


if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        Process_jobs.append(p)

    for job in Process_jobs:
        job.start()

    for job in Process_jobs:
        job.join()
