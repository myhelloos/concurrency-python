#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-03

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

size = comm.size
data = (rank + 1)**2

data = comm.gather(data, root=0)

if rank == 0:
    print("rank = %s ... receiving data from other process" % rank)
    for i in range(1, size):
        # data[i] = (i + 1) ** 2
        value = data[i]
        print(" process %s receiving %s from process %s" % (rank, value, i))