#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-02-03

# usage: mpiexec -n 5 python app/multi-process/helloMPI.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hello world from process", rank)