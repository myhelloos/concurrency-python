#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-01-29

from threading import Thread


def function_to_run():
    import urllib.request
    for i in range(10):
        with urllib.request.urlopen("https://www.baidu.com/") as f:
            f.read(1024)

class threads_object(Thread):
    def run(self):
        function_to_run()

class nothreads_object(object):
    def run(self):
        function_to_run()

def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()

def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))

if __name__ == '__main__':
    import sys
    from timeit import Timer
    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print('start tests')
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat = repeat, number=number))
        show_results("non threaded (%s iters)" % i, best_result)
        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)
        print("Iterations complete")