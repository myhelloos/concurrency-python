#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-03

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

# mpiexec -n 10 python app/multi-process/helloScatter.py
if rank == 9:
    array_to_share = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
else:
    array_to_share = None

recvbuf = comm.scatter(array_to_share, root=9)
print("process = %d recvbuf = %d" % (rank, recvbuf))
