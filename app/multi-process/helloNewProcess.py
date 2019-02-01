#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-01

import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        print("called run method in process: %s" % self.name)
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
