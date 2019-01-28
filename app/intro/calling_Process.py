#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-01-28

## this is the code to execute
import os
dirname = os.path.dirname(__file__)
program = "python"
print("Process calling")
arguments = [dirname + "/called_Process.py"]

## we call the called_Process.py script
os.execvp(program, (program,) + tuple(arguments))
print("Good Bye!!")