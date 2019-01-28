#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: alfred_yuan
# Created on 2019-01-28
from threading import Thread
from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel Python Cookbook!!\n"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Thread Starting\n")
        x = 0
        while (x < 10):
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended\n")

# start the main process
print("Process Started")

# create an instance of the HelloWorld class
hello_python = CookBook()

# print the message...starting the thread
hello_python.start()

# end the main process
print("Process Ended")
