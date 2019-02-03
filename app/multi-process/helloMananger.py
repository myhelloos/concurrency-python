#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-03

import multiprocessing


def worker(dict, key, item):
    dict[key] = item
    print("key = %d value = %d" % (key, item))


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dict = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dict, i, i * 2)) for i in range(10)]
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print("Results: ", dict)
