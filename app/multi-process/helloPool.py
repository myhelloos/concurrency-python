#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-03

import multiprocessing

def function_square(data):
    result = data * data
    return result

if __name__ == '__main__':
    inputs = list(range(101))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print("Pool :", pool_outputs)

