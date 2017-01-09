#!/usr/bin/python
#  -*- coding: latin-1 -*-

num = 1

def par():
    for i in range(10):
        if i % 2 == 0:
            num += 1
    print(num)